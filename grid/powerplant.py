from dataclasses import dataclass
import pygame
from typing import List, Tuple , Optional

@dataclass
class PowerPlant:
    id: int
    fuel: str
    location: Tuple[int, int]
    minproduction: int
    maxproduction: int
    cost: int

    def draw(self,screen):
        pygame.draw.circle(screen, (255, 255, 255),self.location, 20, 0)