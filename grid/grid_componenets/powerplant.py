from dataclasses import dataclass
import pygame
from typing import Tuple
from config import theme
@dataclass
class PowerPlant:

    fuel: str
    location: Tuple[int, int]
    cost: int

    def draw(self, screen):
        pygame.draw.circle(screen, theme['powerplant'], self.location, 20, 0)