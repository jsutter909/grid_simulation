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
        pygame.draw.circle(screen, theme['substation'],self.location, 20, 0)
        