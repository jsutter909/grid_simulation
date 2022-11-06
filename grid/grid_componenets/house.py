from dataclasses import dataclass
import functools
from typing import Tuple, Optional
import enum

import pygame

import config
from adjustments import ConsumptionAdjustment
from grid_componenets.battery import Battery


class Generator(enum.Enum):
    solar = 'solar'
    wind = 'wind'


@dataclass
class House:

    location: Tuple[int, int]
    name: str
    consumption_rate: float
    battery: Battery
    generatorType: Optional[Generator]
    consumption_adjustments: Tuple[ConsumptionAdjustment]

    def __post_init__(self):
        DEFAULT_IMAGE_SIZE = (50, 50)
        image = pygame.image.load('resource/house.png').convert_alpha()
        self.house_img = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

    # Green grid ai here?
    def update(self, time):
        self.battery.charge += self.get_battery_charging(time) * (24 / config.ticksperday)

    def consume(self):
        pass

    def produce(self):
        pass

    def draw(self, screen):
        r = self.house_img.get_rect()
        r.center = self.location
        screen.blit(self.house_img, r)

    def get_usage(self, time):
        return self.consumption_rate \
               + self.get_generation(time) \
               + self.get_battery_charging(time) \
               + sum([adj.get_consumption_adjustment(time) for adj in self.consumption_adjustments])

    def get_battery_charging(self, time):
        charge_tolerance = 0.2 # unit-hours

        target_charge = self.battery.capacity * self.get_battery_charge_target(time)

        if self.battery.charge < target_charge - charge_tolerance:
            return self.battery.charging_rate
        elif target_charge - charge_tolerance < self.battery.charge < target_charge + charge_tolerance:
            return 0
        else:
            return -1 * self.battery.discharging_rate


    def get_generation(self, time):
        return 0

    def get_battery_charge_target(self, time):
        return 0.5