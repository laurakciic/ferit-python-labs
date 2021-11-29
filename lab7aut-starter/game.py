# ukljucivanje biblioteke pygame
import pygame
import random

def center(size, fig):
    figw = fig.get_rect()[2]
    figh = fig.get_rect()[3]
    w = size[0]
    h = size[1]
    return (w/2 - figw/2, h/2 - figh/2)

def middle_x(size, fig, y):
    figw = fig.get_rect()[2]
    figh = fig.get_rect()[3]
    w = size[0]
    return (w/2 - figw/2, y - figh/2)

def load_fig(name, size):
    fig = pygame.image.load(name)
    fig = pygame.transform.scale(fig, size)
    return fig

def render_text(text, size, font="Arial", color=(255,255,255)):
    font = pygame.font.SysFont(font, size)
    return font.render(text, False, color)


def main():
    
    pygame.font.init()
    # definiranje konstanti za velicinu prozora
    WIDTH = 1280
    HEIGHT = 720
    # tuple velicine prozora
    SIZE = (WIDTH, HEIGHT)
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    GREEN = (0,255,0)
    WELCOME_DURATION = 2000

    BG = load_fig("spacebg1.jpg", SIZE)

    #definiranje novog ekrana za igru
    screen = pygame.display.set_mode(SIZE)
    #definiranje naziva prozora
    pygame.display.set_caption("Asteroids")
    #definiranje sata za pracenje fps-a
    clock = pygame.time.Clock()
    welcome_text = render_text("Watch out for the Asteroids!", 96)

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


        
        pygame.display.flip()
        #ukoliko je potrebno ceka do iscrtavanja 
        #iduceg framea kako bi imao 60fpsa
        dt = clock.tick(60)


if __name__ == "__main__":
    main()
    pygame.quit()
