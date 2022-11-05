from dataclasses import dataclass
from typing import List, Tuple , Optional
from colors import *
import pygame

@dataclass
class Substation:
    id: int
    location: Tuple[int, int]
    connectedHouses: List[int]
    connectedPowerPlants: List[int]
    connectedSubstations: List[int]

    # def __post_init__(self):
    #     self.houseImg= pygame.image.load('resources/house.png')

    def draw(self,screen):
        pygame.draw.circle(screen, WHITE,self.location, 20, 0)
        