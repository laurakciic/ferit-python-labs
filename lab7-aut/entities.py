import pygame
import random
import math

class Geometry(object):

    @classmethod
    def get_direction_from_angle(cls, angle, length):
        """ Return x,y direction vector from angle and length"""
        rad_angle = math.radians(angle)
        x = length * math.cos(rad_angle)
        y = length * math.sin(rad_angle)
        return x,y

    @classmethod
    def get_angle_from_line(cls, x1, y1, x2, y2):
        """ Return angle in degrees from two points: 
            
            Params: 
            x1, y1 coordinates for point 1
            x2, y2 coordinates for point 2
        """
        dirx = x2 - x1
        diry = y2 - y1
        rad_angle = math.atan2(diry, dirx)
        deg_angle = rad_angle * 180/math.pi
        return deg_angle % 360

 
class Entity(pygame.sprite.Sprite):
    """
    Main game entity
    Image is defined as a class level variable. Subclasses override their 
    images from the level. Image loading is implemented inside the level
    """
    # Placeholder transparent image
    image = pygame.Surface((100,100), pygame.SRCALPHA, 32)
 
    def __init__(self, level):
        """ Child classes have to configure their images before calling the 
        super().__init__() method, otherwise the object will be initialized 
        with a transparent image
        """

        self.level = level
        self.screen = level.screen
        self.sw, self.sh = self.screen.get_size()
        self.w, self.h = (100,100)
        self.x, self.y = self.sw/2, self.sh/2
        self.angle = random.randint(0,360)
        self.vel = 1
        self.dir = Geometry.get_direction_from_angle(self.angle, self.vel)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.drawn = None

        self.alive = True
 
    def handle_events(self):
        pass
 
    def update(self):
        self.handle_events()
        self.update_direction()
        self.move()
 
 
    def move(self):
        self.x += self.dir[0]
        self.y += self.dir[1]
 
    def update_direction(self):
        self.dir = Geometry.get_direction_from_angle(self.angle, self.vel)
 
    def draw(self):
        img = pygame.transform.scale(self.image, (self.w, self.h))
        img = pygame.transform.rotate(img, -self.angle)
        self.rect = img.get_rect(center = (self.x, self.y))
        self.drawn = self.screen.blit(img, self.rect)
        self.mask = pygame.mask.from_surface(img)

    def collided_with(self, obj):
        return pygame.sprite.collide_mask(self, obj)
 
class Bullet(Entity):
    def __init__(self, level, x, y, angle, turret=False):
        if turret:
            self.image = level.TURRET_LASER
        else:
            self.image = level.LASER
        super().__init__(level)
        self.w, self.h = (25, 6)
        self.angle = angle
        self.x, self.y = x,y
        self.vel = 10

    def handle_events(self):
        if self.x < 0 or self.x > self.sw:
            self.alive = False
        if self.y < 0 or self.y > self.sh:
            self.alive = False
        
 
 
 
class Player(Entity):
    """Handles all the logic for the player object"""
    SHIP_VELOCITY = 5
    CANNON_COOLDOWN = 8
 
    def __init__(self, level):
        self.image = level.SHIP_OFF
        self.mask_img = level.SHIP_OFF
        super().__init__(level)
        self.image_on = level.SHIP_ON
        self.image_off = level.SHIP_OFF
        self.w, self.h = (150, 50)
        self.angle = 0
        self.vel = 0
        self.cannon_cooldown = self.CANNON_COOLDOWN
 
    def handle_events(self):
        # calculate direction from mouse position
        mousepos = pygame.mouse.get_pos()
        self.angle = Geometry.get_angle_from_line(self.x, self.y, mousepos[0], mousepos[1])

        mouse_pressed = pygame.mouse.get_pressed()
        self.fire(mouse_pressed)

        
        keys = pygame.key.get_pressed()
        self.vel = 0
        if keys[pygame.K_w]:
            self.vel = self.SHIP_VELOCITY
        elif keys[pygame.K_s]:
            self.vel = - self.SHIP_VELOCITY

        if self.vel == 0:
            self.image = self.image_off
        else:
            self.image = self.image_on


    def fire(self, mouse_pressed):
        self.cannon_cooldown -= 1
        if self.cannon_cooldown <= 0:
            if mouse_pressed[0]:
                bullet_dir = Geometry.get_direction_from_angle(self.angle, self.w/2)
                bullet_x = self.x + bullet_dir[0]
                bullet_y = self.y + bullet_dir[1]
                self.level.bullets.append(Bullet(self.level, bullet_x, bullet_y, self.angle))
                self.cannon_cooldown = self.CANNON_COOLDOWN 

    def draw(self):
        if self.alive:
            img = pygame.transform.scale(self.image, (self.w, self.h))
            img = pygame.transform.rotate(img, -self.angle)
            self.rect = img.get_rect(center = (self.x, self.y))
            self.drawn = self.screen.blit(img, self.rect)
            maskimg = pygame.transform.scale(self.mask_img, (self.w, self.h))
            maskimg = pygame.transform.rotate(maskimg, -self.angle)
            self.mask = pygame.mask.from_surface(maskimg)
 
class Asteroid(Entity):
    """Handles all the logic for the asteroid object"""
    PLAYER_DEAD_ZONE = 100
 
    def __init__(self, level):
        self.image = level.ASTEROID
        self.mask_img = level.ASTEROID_MASK
        super().__init__(level)
        self.w, self.h = (100, 45)
        self.vel = 2
        self.radius = 30
        self.init_random_position()
 
    def handle_events(self):
        dirx = self.dir[0]
        diry = self.dir[1]
        if self.x < self.radius or self.x > self.sw - self.radius:
            dirx *= -1
        if self.y < self.radius or self.y > self.sh - self.radius:
            diry *= -1
        self.angle = Geometry.get_angle_from_line(0,0,dirx,diry)
        self.dir = Geometry.get_direction_from_angle(self.angle, self.vel)
 
    def init_random_position(self):
        """
        Create x,y coordinates that are at least PLAYER_DEAD_ZONE pixels away
        from the player (center of the screen)."""
        left = random.randint(self.radius, self.sw/2 - self.PLAYER_DEAD_ZONE)
        right = random.randint(self.sw/2+self.PLAYER_DEAD_ZONE, self.sw - self.radius)
        top = random.randint(self.radius, self.sh/2 - self.PLAYER_DEAD_ZONE)
        bottom = random.randint(self.sh/2+self.PLAYER_DEAD_ZONE, self.sh - self.radius)
        self.x = random.choice( [left, right] )
        self.y = random.choice( [top, bottom] )

class Turret(Entity):
    """Handles all the logic for the player object"""
    CANNON_COOLDOWN = 45
 
    def __init__(self, level):
        self.image = level.TURRET
        super().__init__(level)
        self.w, self.h = (150, 80)
        self.x, self.y = (50, 50)
        self.angle = 0
        self.vel = 0
        self.cannon_cooldown = self.CANNON_COOLDOWN
 
    def handle_events(self):
        # calculate direction from mouse position
        self.angle = Geometry.get_angle_from_line(self.x, self.y, self.level.player.x, self.level.player.y)

        self.fire()


    def fire(self):
        self.cannon_cooldown -= 1
        if self.cannon_cooldown <= 0:
            bullet_dir = Geometry.get_direction_from_angle(self.angle, self.w/2)
            bullet_x = self.x + bullet_dir[0]
            bullet_y = self.y + bullet_dir[1]
            self.level.turret_bullets.append(
                    Bullet(self.level, bullet_x, bullet_y, self.angle, turret=True)
            )
            self.cannon_cooldown = self.CANNON_COOLDOWN 
