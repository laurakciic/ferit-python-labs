# ukljucivanje biblioteke pygame
import pygame

pygame.init()
# definiranje konstanti za velicinu prozora
WIDTH = 1024
HEIGHT = 600
# tuple velicine prozora
size = (WIDTH, HEIGHT)

#definiranje novog ekrana za igru
screen = pygame.display.set_mode(size)
#definiranje naziva prozora
pygame.display.set_caption("Nasa kul igra")

clock = pygame.time.Clock()

done = False
while not done:
    #event petlja
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()

    #ukoliko je potrebno ceka do iscrtavanja 
    #iduceg framea kako bi imao 60fpsa
    clock.tick(60)

pygame.quit()
