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
 
    def __init__(self, screen, image):
        self.screen = screen
        self.sw, self.sh = screen.get_size()
        self.w, self.h = (100,100)
        self.x, self.y = self.sw/2, self.sh/2
        self.angle = random.randint(0,360)
        self.vel = 1
        self.dir = Geometry.get_direction_from_angle(self.angle, self.vel)
        self.image = image
        self.drawn = None
 
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
 
class Bullet(Entity):
    def __init__(self, screen, image, x, y, angle):
        super().__init__(screen, image)
        self.w, self.h = (25, 6)
        self.angle = angle
        self.x, self.y = x,y
        self.vel = 10
 
 
 
class Player(Entity):
    """Handles all the logic for the player object"""
    SHIP_VELOCITY = 3
 
    def __init__(self, screen, image_on, image_off, bullet_image):
        super().__init__(screen, image_off)
        self.image_on = image_on
        self.image_off = image_off
        self.w, self.h = (150, 50)
        self.angle = 0
        self.vel = 0
        self.bullets = []
        self.bullet_image = bullet_image
 
    def handle_events(self):
        # calculate direction from mouse position
        mousepos = pygame.mouse.get_pos()
        self.angle = Geometry.get_angle_from_line(self.x, self.y, mousepos[0], mousepos[1])

        keys = pygame.key.get_pressed()

        mouse_pressed = pygame.mouse.get_pressed()
        self.fire(mouse_pressed)

        for bullet in self.bullets:
            if bullet.x < 0 or bullet.x > self.sw:
                self.bullets.remove(bullet)
            if bullet.y < 0 or bullet.y > self.sh:
                self.bullets.remove(bullet)
 
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
        if mouse_pressed[0]:
            self.bullets.append(Bullet(self.screen, self.bullet_image, self.x, self.y, self.angle))
 
 
class Asteroid(Entity):
    """Handles all the logic for the asteroid object"""
    PLAYER_DEAD_ZONE = 100
 
    def __init__(self, screen, image):
        super().__init__(screen, image)
        self.w, self.h = (100, 45)
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
