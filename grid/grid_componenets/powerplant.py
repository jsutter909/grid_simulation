from dataclasses import dataclass
import pygame
from typing import Tuple

@dataclass
class PowerPlant:

    fuel: str
    location: Tuple[int, int]
    cost: int

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.location, 20, 0)