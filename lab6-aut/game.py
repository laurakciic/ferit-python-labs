# ukljucivanje biblioteke pygame
import pygame
import random
from entities import Player, Asteroid
from helpers import *


def main():
    
    pygame.font.init()
    # definiranje konstanti za velicinu prozora
    WIDTH = 1600
    HEIGHT = 900
    # tuple velicine prozora
    SIZE = (WIDTH, HEIGHT)
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    GREEN = (0,255,0)
    WELCOME_DURATION = 300
    ASTEROID_COUNT = 10

    BG = load_fig("spacebg1.jpg", SIZE)
    SHIP_ON = pygame.image.load("ship_on.png")
    SHIP_OFF = pygame.image.load("ship_off.png")
    ASTEROID = pygame.image.load("asteroid.png")
    LASER = pygame.image.load("laser.png")
    
    #definiranje novog ekrana za igru
    screen = pygame.display.set_mode(SIZE)
    #definiranje naziva prozora
    pygame.display.set_caption("Asteroids")
    #definiranje sata za pracenje fps-a
    clock = pygame.time.Clock()
    welcome_text = render_text("Watch out for the Asteroids!", 96)

    player = Player(screen, SHIP_ON, SHIP_OFF, LASER)
    asteroids = [ Asteroid(screen, ASTEROID) for i in range(ASTEROID_COUNT) ]

    state = "welcome"
    welcome_timeout = WELCOME_DURATION
    dt = 0
    score = 0
    done = False
    while not done:
        #event petlja
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        #state processing
        if state == "welcome":
            welcome_timeout -= dt
            if welcome_timeout - dt <= 0:
                state = "game"
                welcome_timeout = WELCOME_DURATION

        elif state == "game":
            pass

        #iscrtavanja
        if state == "welcome":
            screen.blit(BG, (0,0))
            screen.blit(welcome_text, center(SIZE, welcome_text))
            timeout = render_text("%.2f"%(welcome_timeout/1000), 48)
            screen.blit( timeout, middle_x(SIZE, timeout, 200))

        elif state == "game":
            screen.blit(BG, (0,0))
            screen.blit(render_text("Score: %d"%score,20), (20,20))

            for asteroid in asteroids:
                asteroid.update()
                asteroid.draw()

            player.update()
            for bullet in player.bullets:
                bullet.update()
                bullet.draw()
            player.draw()
        
        pygame.display.flip()
        #ukoliko je potrebno ceka do iscrtavanja 
        #iduceg framea kako bi imao 60fpsa
        dt = clock.tick(60)


if __name__ == "__main__":
    main()
    pygame.quit()
