import pygame
import random
from entities import Player, Asteroid, Turret
from helpers import render_text

class Level(object):
    LEVEL_START_TIMEOUT = 60
    CONFIG = {
        1: {"asteroid_count": 5 },
        2: {"asteroid_count": 8 },
        3: {"asteroid_count": 10},
        4: {"asteroid_count": 13},
        5: {"asteroid_count": 13},
        6: {"asteroid_count": 15},
        7: {"asteroid_count": 20},
        8: {"asteroid_count": 25},
    }
    SHIP_ON = pygame.image.load("ship_on.png")
    SHIP_OFF = pygame.image.load("ship_off.png")
    ASTEROID = pygame.image.load("asteroid.png")
    ASTEROID_MASK = pygame.image.load("asteroid_mask.png")
    LASER = pygame.image.load("laser.png")
    TURRET = pygame.image.load("turret.png")
    TURRET_LASER = pygame.image.load("turret_laser.png")
    EXPLOSION_SHEET = pygame.image.load("explosion.png")

    def __init__(self, screen, level):
        self.frame = 0
        self.screen = screen
        self.sw, self.sh = self.screen.get_size()
        self.state = "play" # "play", "won", "lost"
        self.score = 0

        self.player = Player(self)
        self.turret = Turret(self)

        self.ASTEROID_COUNT = self.CONFIG[level]["asteroid_count"]
        self.asteroids = []
        for i in range(self.ASTEROID_COUNT):
               self.asteroids.append( Asteroid(self))

        self.bullets = []
        self.turret_bullets = []
        
    def update(self):
        self.frame += 1
        for asteroid in self.asteroids:
            asteroid.update()
        self.player.update()
        for bullet in self.bullets:
            bullet.update()
        self.turret.update()
        for bullet in self.turret_bullets:
            bullet.update()

        self.check_collisions()
        self.clear_dead_entities()

        for asteroid in self.asteroids:
            asteroid.draw()
        for bullet in self.bullets:
            bullet.draw()
        for bullet in self.turret_bullets:
            bullet.draw()
        self.player.draw()
        self.turret.draw()

        bullet_count = render_text("Bullets: %d"%len(self.bullets), 16)
        self.screen.blit(bullet_count, (20, self.sh-36))

        #Handle states
        if not self.player.alive:
            self.state = "lost"
        if len(self.asteroids) == 0:
            self.state = "won"

    def check_collisions(self):
        if self.frame < self.LEVEL_START_TIMEOUT:
            return False
        for asteroid in self.asteroids:
            for bullet in self.bullets:
                if bullet.collided_with(asteroid):
                    bullet.alive = False
                    asteroid.alive = False
                    self.score += 1
            if self.player.collided_with(asteroid):
                asteroid.alive = False
                self.player.alive = False

    def clear_dead_entities(self):
        for i, bullet in enumerate(self.bullets):
            if not bullet.alive:
                del self.bullets[i]

        for i, asteroid in enumerate(self.asteroids):
            if not asteroid.alive:
                del self.asteroids[i]
