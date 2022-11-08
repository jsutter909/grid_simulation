from dataclasses import dataclass
from typing import Tuple
from colors import *
import pygame
from pygame.math import Vector2

from config import orb_center_distance, orb_radius, theme

@dataclass
class PowerLine:

    start: Tuple[int, int]
    finish: Tuple[int, int]
    flow: int # if positive, its to the finish. if negative, its from the finish

    def __post_init__(self):
        self.offset = 0

    def draw(self,screen):
        start = Vector2(self.start)
        finish = Vector2(self.finish)
        
        start = start.move_towards(finish,20)
        finish = finish.move_towards(start,20)

        if self.flow != 0:

            length = start.distance_to(finish)
            orbs = int(length//orb_center_distance)
            orb_speed = self.flow

            orbstart = start.move_towards(finish, self.offset)

            for i in range(orbs):
                pygame.draw.circle(screen, YELLOW ,orbstart, orb_radius, 0)
                orbstart = orbstart.move_towards(finish, orb_center_distance)

            self.offset = (self.offset + orb_speed) % orb_center_distance
        pygame.draw.line(screen, theme['powerline'], start, finish, 2)


    def update(self,flow):
        pass
