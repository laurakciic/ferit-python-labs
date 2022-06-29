import pygame
import random
from entities import Player, Asteroid, Turret, Explosion, LaserHit, HealthPack
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
    HEALTH_PACK = pygame.image.load("pack.png")

    def __init__(self, screen, level):
        self.frame = 0
        self.screen = screen
        self.sw, self.sh = self.screen.get_size()
        self.state = "play" # "play", "won", "lost"
        self.score = 0

        self.player = Player(self)
        self.turrets = []
        for i in range(2):
            self.turrets.append( Turret(self) )
        self.healthpacks = []
        self.healthpacks.append( HealthPack(self) )

        self.ASTEROID_COUNT = self.CONFIG[level]["asteroid_count"]
        self.asteroids = []
        for i in range(self.ASTEROID_COUNT):
               self.asteroids.append( Asteroid(self))

        self.bullets = []
        self.turret_bullets = []
        self.explosions = []
        

    def update(self):
        self.frame += 1
        for asteroid in self.asteroids:
            asteroid.update()
        self.player.update()
        for bullet in self.bullets:
            bullet.update()
        for turret in self.turrets:
            turret.update()
        for bullet in self.turret_bullets:
            bullet.update()
        for e in self.explosions:
            e.update()
        for HealthPack in self.healthpacks:
            HealthPack.update()

        self.check_collisions()
        self.clear_dead_entities()

        for asteroid in self.asteroids:
            asteroid.draw()
        for bullet in self.bullets:
            bullet.draw()
        for bullet in self.turret_bullets:
            bullet.draw()
        self.player.draw()
        for turret in self.turrets:
            turret.draw()
        for e in self.explosions:
            e.draw()
        for HealthPack in self.healthpacks:
            HealthPack.draw()

        bullet_count = render_text("Bullets: %d"%len(self.bullets), 16)
        self.screen.blit(bullet_count, (20, self.sh-36))
        health = render_text("Health: %d"%self.player.health, 20)
        self.screen.blit(health, (20,60))
        if self.player.teleport_cooldown > 0:
            postotak = render_text("Teleport: %d %%"%self.player.postotak , 40)
            self.screen.blit(postotak, (20, self.sh-100))
        if self.player.postotak == 100:
            postotak = render_text("Teleport: READY!!", 40)
            self.screen.blit(postotak, (20, self.sh-100))

        turrets_health = " | ".join([ str(turret.health) for turret in self.turrets ])
        turrets_health = "Turrets: %s"%turrets_health
        self.screen.blit(render_text(turrets_health, 20), (20,100))

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
                    self.explosions.append(Explosion(asteroid))

            if self.player.collided_with(asteroid):
                asteroid.alive = False
                self.player.alive = False

        for bullet in self.turret_bullets:
            if bullet.collided_with(self.player):
                self.explosions.append(LaserHit(bullet))
                self.player.hit()
                bullet.alive = False
        for bullet in self.bullets:
            for turret in self.turrets:
                if bullet.collided_with (turret):
                    self.explosions.append(LaserHit(bullet))
                    bullet.alive = False
                    turret.hit()
                    if turret.alive == False:
                        self.explosions.append(Explosion(turret))
        for turret in self.turrets:
            if self.player.collided_with(turret):
                turret.alive = False
                self.player.alive = False
        
        for HealthPack in self.healthpacks:
            if self.player.collided_with(HealthPack):
                self.player.heal()
                HealthPack.alive = False


    def clear_dead_entities(self):
        for i, bullet in enumerate(self.bullets):
            if not bullet.alive:
                del self.bullets[i]

        for i, asteroid in enumerate(self.asteroids):
            if not asteroid.alive:
                del self.asteroids[i]

        for i, bullet in enumerate(self.turret_bullets):
            if not bullet.alive:
                del self.turret_bullets[i]

        for i, turret in enumerate(self.turrets):
            if not turret.alive:
                del self.turrets[i]

        for i, explosion in enumerate(self.explosions):
            if not explosion.alive:
                del self.explosions[i]
        
        for i, HealthPack in enumerate(self.healthpacks):
            if not HealthPack.alive:
                del self.healthpacks[i]
