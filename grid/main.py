import pygame

from colors import *
from environment import *
from grid_componenets.gridFactory import *
from app import *
from config import *

pygame.init()

w = 1920
h = 1080
size = (w, h)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Power Network")

done = False
clock = pygame.time.Clock()

timesteps = ticks_per_day * 7
env = Environment(timesteps)

grid = GridFactory.get_grid(env)

infomenu = InfoMenu((w - 500, 0), (100, w - 400), env)

app = App(grid, infomenu)
time = 0

RUNNING, PAUSE = 0, 1
state = RUNNING

def drawSimOver(screen):
        r = pygame.Rect(layout['simover'])
        rect = screen.get_rect()
        r.center = rect.center
        pygame.draw.rect(screen,BLACK,r)
        font = pygame.font.SysFont(None, 48)
        s = "Simulation Complete"
        img = font.render(s, True, RED)
        screen.blit(img, (r.centerx-img.get_width()/2,r.centery-img.get_height()/2))

while not done:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state=1-state
    
    if time>=timesteps:
        state=PAUSE
        drawSimOver(screen)
        pygame.display.flip()
    if state==RUNNING:
        

        screen.fill(theme['background'])
        if time < timesteps:
            app.update(time)

        app.draw(screen, time)
        time += 1
        pygame.display.flip()

    clock.tick(33)  # Each tick represents 5 minutes

pygame.quit()

