# ukljucivanje biblioteke pygame
import pygame
import random
#from entities import Player, Asteroid
from level import Level
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
    WELCOME_DURATION = 1250
    

    BG = load_fig("spacebg1.jpg", SIZE)
    
    
    #definiranje novog ekrana za igru
    screen = pygame.display.set_mode(SIZE)
    #definiranje naziva prozora
    pygame.display.set_caption("Asteroids")
    #definiranje sata za pracenje fps-a
    clock = pygame.time.Clock()

    welcome_text = render_text("Watch out for the Asteroids!", 96)
    gameover_text = render_text("YOU LOST!", 96)


    state = "welcome"
    welcome_timeout = WELCOME_DURATION
    dt = 0
    current_level = 1
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
                level = Level(screen, current_level)

        elif state == "game":
            if level.state == "lost":
                state = "gameover"
                current_level = 1
            elif level.state == "won":
                state = "level_passed"
                level_passed_text = render_text("You passed level %s"%current_level, 96)
                current_level += 1

        elif state == "gameover":
            welcome_timeout -= dt
            if welcome_timeout - dt <= 0:
                state = "welcome"
                welcome_timeout = WELCOME_DURATION

        elif state == "level_passed":
            welcome_timeout -= dt
            if welcome_timeout - dt <= 0:
                state = "welcome"
                welcome_timeout = WELCOME_DURATION

        #iscrtavanja
        screen.blit(BG, (0,0))
        if state == "welcome":
            screen.blit(welcome_text, center(SIZE, welcome_text))
            timeout = render_text("%.2f"%(welcome_timeout/1000), 48)
            screen.blit( timeout, middle_x(SIZE, timeout, 200))
            level_text = render_text("LEVEL %d"%(current_level), 48)
            screen.blit( level_text, middle_x(SIZE, timeout, HEIGHT/4*3))

        elif state == "game":
            level.update()
            
        if state == "gameover":
            screen.blit(gameover_text, center(SIZE, gameover_text))
        
        if state == "level_passed":
            screen.blit(level_passed_text, center(SIZE, level_passed_text))

        pygame.display.flip()
        #ukoliko je potrebno ceka do iscrtavanja 
        #iduceg framea kako bi imao 60fpsa
        dt = clock.tick(60)

if __name__ == "__main__":
    main()
    pygame.quit()
