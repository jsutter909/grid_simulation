import pygame
from math import *
from random import randint, random

from worldFactory import *

import matplotlib

matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import pylab


pygame.init()

w = 1920
h = 1080
size = (w, h)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Power Network")


done = False
clock = pygame.time.Clock()


world = WorldFactory.getWorld()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    world.update()
    world.draw(screen)

    pygame.display.flip()

    clock.tick(33) #Each tick represents 5 minutes

pygame.quit()
