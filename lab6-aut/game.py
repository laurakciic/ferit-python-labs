# ukljucivanje biblioteke pygame
import pygame

pygame.init()
# definiranje konstanti za velicinu prozora
WIDTH = 1024
HEIGHT = 600
import random
WHITE = (255,255,255)
# tuple velicine prozora
size = (WIDTH, HEIGHT)
myfont = pygame.font.SysFont('Arial',40)
text = myfont.render("Welcome", True, WHITE)
text1 = myfont.render("Game Over", True, WHITE)
#definiranje novog ekrana za igru
screen = pygame.display.set_mode(size)
#definiranje naziva prozora
pygame.display.set_caption("Nasa kul igra")

clock = pygame.time.Clock()
center = [WIDTH/2 - text.get_width()/2 , HEIGHT/2 - text.get_height()/2 ]
bgimg = pygame.image.load("bg.jpg")
bgimg = pygame.transform.scale( bgimg, (WIDTH, HEIGHT))
icon = pygame.image.load("icon.png")
icon = pygame.transform.scale(icon, (100,100))
icon_pos = [WIDTH/2 - icon.get_width()/2 , HEIGHT/2 - icon.get_height()/2 ]
dx = -1
dy = 1
time = 0
done = False
state = "welcome" # welcome, game, gameover

while not done:
    hit=False
    #event petlja
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = event.pos
            if icon_drawn.collidepoint(click_pos):
                hit = True 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                icon_pos[0] = random.randint(0,1000)
                icon_pos[1] = random.randint(0,400)
            if event.key == pygame.K_RETURN:
                if state == "welcome":
                    state = "game"
                if state == "gameover":
                    time = 0
                    state = "welcome"
            if event.key == pygame.K_ESCAPE:
                if state == "welcome":
                    done = True
                elif state == "game":
                    state = "gameover"
                elif state == "gameover":
                    done = True
            

    if state == "welcome":
        if time > 3000:
            state = "game"
    elif state == "game":
        if icon_pos[0] >= WIDTH - icon.get_width():
            dx = -1
        if icon_pos[1] >= HEIGHT - icon.get_height():
            dy = -1
        if icon_pos[0] <= 0:
            dx = 1
        if icon_pos[1] <= 0:
            dy = 1
        icon_pos[0] = icon_pos [0]  + dx
        icon_pos[1] = icon_pos [1]  + dy

        if hit:
            icon_pos[0] = random.randint(0, WIDTH-100)
            icon_pos[1] = random.randint(0,HEIGHT-100)

    if state == "welcome":
        screen.blit(bgimg, (0, 0))
        screen.blit(text, center)
    elif state == "game":
        screen.blit(bgimg, (0, 0))
        icon_drawn= screen.blit(icon, (icon_pos[0], icon_pos[1]))
    elif state == "gameover":
        screen.blit(bgimg, (0, 0))
        screen.blit(text1, center)
    #ukoliko je potrebno ceka do iscrtavanja 
    #iduceg framea kako bi imao 60fpsa
    dt = clock.tick(60)
    time += dt
    pygame.display.flip()

pygame.quit()
