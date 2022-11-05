from dataclasses import dataclass
from typing import Tuple
from colors import *
import pygame
from pygame.math import Vector2

@dataclass
class PowerLine:
    start: Tuple[int, int]
    finish: Tuple[int, int]
    def __post_init__(self):
        self.flow = -1 
        self.count = 0

    def draw(self,screen):
        start = Vector2(self.start)
        finish = Vector2(self.finish)
        #start = start.move_towards(finish,20)
        #finish = finish.move_towards(start,20)
        length = start.distance_to(finish)
        orbs = int(length//10)

        speed = self.count + self.flow
        orbstart = start.move_towards(finish,speed)
        for i in range(orbs):
            pygame.draw.circle(screen, YELLOW ,orbstart, 5, 0)
            orbstart = orbstart.move_towards(finish,orbs)

        pygame.draw.line(screen, WHITE, start, finish, 2)
        self.count = (self.count+self.flow)%orbs

    def update(self,flow):
        pass
