# ukljucivanje biblioteke pygame
import pygame
import random

def center(size, fig):
    figw = fig.get_rect()[2]
    figh = fig.get_rect()[3]
    w = size[0]
    h = size[1]
    return (w/2 - figw/2, h/2 - figh/2)
    
def load_fig(name, size):
    fig = pygame.image.load(name)
    fig = pygame.transform.scale(fig, size)
    return fig

    
pygame.init()
# definiranje konstanti za velicinu prozora
WIDTH = 1024
HEIGHT = 600
# tuple velicine prozora
size = (WIDTH, HEIGHT)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)

#definiranje novog ekrana za igru
screen = pygame.display.set_mode(size)

#definiranje naziva prozora
pygame.display.set_caption("lkasdla")

myfont = pygame.font.SysFont('Arial', 30)
welcome_text= myfont.render("Welcome to my game", False, BLACK)
end_text = myfont.render("GAME OVER", True, WHITE)

welcome_bg = load_fig("bg.jpg", size)
end_bg = load_fig("end.jpg", size)
bobimg = load_fig("bob.png", (100,100))


clock = pygame.time.Clock()

state = "welcome"
bg= RED
bobx, boby = center(size, bobimg)
done = False
while not done:
    #event petlja
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if state == "game":
                pos = event.pos
                if bob.collidepoint(pos):
                    hit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if state == "game":
                    if bg == GREEN:
                        bg = RED
                    elif bg == RED:
                        bg = BLACK
                    elif bg == BLACK:
                        bg = GREEN
                elif state == "end":
                    state = "welcome"
            elif event.key == pygame.K_RETURN:
                if state == "welcome":
                    state = "game"
            elif event.key == pygame.K_ESCAPE:
                if state == "game":
                    state = "end"
    #state processing
    if state == "game":
        bobx += dx
        boby += dy
        if bobx > WIDTH - 100 or bobx <0:
            dx = dx * -1
        if boby > HEIGHT - 100 or boby <0:
            dy = dy * -1

        game_time -= clock.get_time()
        if game_time < 0:
            state = "end"
        if hit:
            bobx = random.randint(0, WIDTH - 100)
            boby = random.randint(0, HEIGHT - 100)
            game_time_start *= 0.9
            game_time = game_time_start
            score += 1
            hit = False
    elif state == "welcome":
        game_time_start = 3000
        game_time = game_time_start
        bobx, boby = center(size,bobimg)
        hit = False
        dx = 1
        dy = 1
        score = 0


    #iscrtavanja
    if state == "welcome":
        screen.blit(welcome_bg, (0,0))
        screen.blit(welcome_text, center(size, welcome_text))
    elif state == "game":
        screen.fill(bg)
        bob = screen.blit(bobimg, (bobx,boby))
        time = myfont.render("Time: %d"%game_time, True, WHITE)
        screen.blit(time, (30, HEIGHT - 100))
        score_text = myfont.render("Score: %d"%score, True, WHITE)
        screen.blit(score_text, (30, 30))
    elif state == "end":
        screen.blit(end_bg, (0,0))
        screen.blit(end_text, center(size, end_text))    
    
    pygame.display.flip()

    #ukoliko je potrebno ceka do iscrtavanja 
    #iduceg framea kako bi imao 60fpsa
    clock.tick(60)

pygame.quit()
