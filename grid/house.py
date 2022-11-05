from dataclasses import dataclass
from typing import List, Tuple, Optional
import enum

import pygame

from adjustments import ConsumptionAdjustment


class Generator(enum.Enum):
    solar = 'solar'
    wind = 'wind'


@dataclass
class House:
    id: int
    location: Tuple[int, int]
    name: str
    consumption_rate: float
    generatorType: Optional[Generator]
    consumption_adjustments: List[ConsumptionAdjustment]

    def __post_init__(self):
        DEFAULT_IMAGE_SIZE = (50, 50)
        image = pygame.image.load('resource/house.png').convert_alpha()
        self.houseImg = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

    # Green grid ai here?
    def update(self, world):
        pass

    def consume(self):
        pass

    def produce(self):
        pass

    def draw(self, screen):
        r = self.houseImg.get_rect()
        r.center = self.location
        screen.blit(self.houseImg, r)

    def get_battery_charging(self, time):
        return 0

    def get_generation(self, time):
        return 0

    def get_useage(self, time):
        return self.consumption_rate \
               + self.get_generation(time) \
               + self.get_battery_charging(time) \
               + sum([adj.get_consumption_adjustment(time) for adj in self.consumption_adjustments])