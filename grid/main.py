import pygame
from math import *
from random import randint, random

from network import *

from gridFactory import *

import matplotlib

matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import pylab

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)

pygame.init()

w = 1024
h = 768
size = (w, h)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Power Network")


done = False
clock = pygame.time.Clock()


powergrid = gridFactory.getNetwork()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    for n in powergrid.nodes:
        x0,y0 = n.location
        for j in n.connected: 
            x1,y1 = powergrid.getNodeById(j).location
            pygame.draw.line(screen, GREY, [x0, y0], [x1, y1], 2)

    
    for n in powergrid.nodes:
        radius = 50
        x = n.location[0]- radius/2
        y = n.location[1] - radius/2
        if radius > 1:
            pygame.draw.ellipse(screen, WHITE, [x, y, radius, radius], 1)

    pygame.display.flip()

    clock.tick(33) #Each tick represents 5 minutes

pygame.quit()
