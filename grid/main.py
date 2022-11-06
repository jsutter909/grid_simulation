import pygame

from colors import BLACK
from environment import *
from grid_componenets.gridFactory import *
from app import *
from config import ticksperday

pygame.init()

w = 1920
h = 1080
size = (w, h)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Power Network")

done = False
clock = pygame.time.Clock()

timesteps = ticksperday * 7
env = Environment(timesteps)

grid = GridFactory.get_grid(env)

infomenu = InfoMenu((w - 500, 100), (100, w - 400), env)

app = App(grid, infomenu)
time = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    time += 1

    screen.fill(BLACK)
    if time < timesteps:
        app.update(time)

    app.draw(screen, time)
    pygame.display.flip()

    clock.tick(33)  # Each tick represents 5 minutes

pygame.quit()
