from dataclasses import dataclass
from typing import Tuple
from config import theme
import pygame

@dataclass
class Substation:
    location: Tuple[int, int]

    # def __post_init__(self):
    #     self.houseImg= pygame.image.load('resources/house.png')

    def draw(self, screen):
        r = pygame.Rect(1,1,60,60)
        r.center = self.location
        #pygame.draw.circle(screen, theme['substation'],self.location, 20, 0)
        pygame.draw.rect(screen,theme['substation'],r)
