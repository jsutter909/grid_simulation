from dataclasses import dataclass
import pygame
from typing import Tuple
import config
@dataclass
class PowerPlant:

    fuel: str
    location: Tuple[int, int]
    cost: int

    def draw(self, screen):
        pygame.draw.circle(screen, config.theme['powerplant'], self.location, 30, 0)
        font = pygame.font.SysFont(None, 30)
        img = font.render(self.fuel, True, config.theme['text'])
        screen.blit(img, (self.location[0]-img.get_width()/2,self.location[1]+40))