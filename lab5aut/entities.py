import pygame
import random

class Player(object):
    """Handles all the logic for the player object"""

    def __init__(self, screen, image):
        self.screen = screen
        self.sw, self.sh = screen.get_size()
        self.w, self.h = (70, 100)
        self.x, self.y = self.sw/2, self.sh/2
        self.dx, self.dy = 1,1
        self.image = image
        self.drawn = None

    def update(self):
        self.rect = pygame.Rect(self.x - self.w/2, self.y-self.h/2, self.w, self.h)

    def draw(self):
        ship_img = pygame.transform.scale(self.image, (self.w, self.h))
        self.drawn = self.screen.blit(ship_img, self.rect)

class Asteroid(object):
    """Handles all the logic for the player object"""
    PLAYER_DEAD_ZONE = 300

    def __init__(self, screen):
        self.screen = screen
        self.sw, self.sh = screen.get_size()
        self.radius = random.randint(10,40)
        self.init_random_position()
        self.dx, self.dy = random.choice([-1,1]), random.choice([-1,1])

    def update(self):
        #self.rect = pygame.Rect(self.x - self.w/2, self.y-self.h/2, self.w, self.h)
        self.move()

    def draw(self):
        pygame.draw.circle(self.screen, (33,33,33), (self.x, self.y), self.radius)

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

    def move(self):
        if self.x >= self.sw - self.radius or self.x <= self.radius:
            self.dx *= -1
        if self.y >= self.sh - self.radius or self.y <= self.radius:
            self.dy *= -1
        self.x = self.x + self.dx
        self.y = self.y + self.dy


