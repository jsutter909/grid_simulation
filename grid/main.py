import pygame

from infomenu import InfoMenu
from gridFactory import *
from app import *


pygame.init()

w = 1920
h = 1080
size = (w, h)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Power Network")


done = False
clock = pygame.time.Clock()


grid = GridFactory.get_grid()

infomenu = InfoMenu((w-500,100),(100,w-400))

app = App(grid,infomenu)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    app.update()
    app.draw(screen)
    pygame.display.flip()

    clock.tick(33) #Each tick represents 5 minutes

pygame.quit()
