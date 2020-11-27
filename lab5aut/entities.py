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
        size = random.randint(50,150)
        self.w, self.h = (size, size)
        self.init_random_position()
        self.dx, self.dy = 1,1

    def update(self):
        self.rect = pygame.Rect(self.x - self.w/2, self.y-self.h/2, self.w, self.h)

    def draw(self):
        pygame.draw.rect(self.screen, (66,66,66), self.rect)

    def init_random_position(self):
        """
        Create x,y coordinates that are at least PLAYER_DEAD_ZONE pixels away
        from the player (center of the screen)."""
        self.x = random.randint(0, self.sw)
        self.y = random.randint(0, self.sh)


