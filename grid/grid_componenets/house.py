from dataclasses import dataclass
from typing import Tuple, Optional
import enum

import pygame

import config
import green_grid_ai.ai
from adjustments import ConsumptionAdjustment
from graph_store import GraphStore
from grid_componenets.battery import Battery


class Generator(enum.Enum):
    solar = 'solar'
    wind = 'wind'

labels = ["usage", "target_charge", "battery_charge"]

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
        self.green_grid_AI = green_grid_ai.ai.BatteryTargetAI(self)
        self.graph_store = GraphStore(labels, 0, config.tick_to_hour(1))

    # Green grid ai here?
    def update(self, grid, time):
        self.graph_store.publish([
            self.get_usage(grid, time),
            self.get_battery_charge_target(grid, time),
            self.battery.charge])
        self.battery.charge += self.get_battery_charging(grid, time) * config.tick_to_hour(1)

    def consume(self):
        pass

    def produce(self):
        pass

    def draw(self, screen):
        r = self.house_img.get_rect()
        r.center = self.location
        screen.blit(self.house_img, r)

    def get_non_battery_useage(self, time):
        return self.consumption_rate \
               + self.get_generation(time) \
               + sum([adj.get_consumption_adjustment(time) for adj in self.consumption_adjustments])

    def get_usage(self, grid, time):
        return self.get_non_battery_useage(time) + self.get_battery_charging(grid, time)

    def get_battery_charging(self, grid, time):
        charge_tolerance = 0.2 # unit-hours

        target_charge = self.battery.capacity * self.get_battery_charge_target(grid, time)

        if self.battery.charge < target_charge - charge_tolerance:
            return self.battery.charging_rate
        elif target_charge - charge_tolerance < self.battery.charge < target_charge + charge_tolerance:
            return 0
        else:
            return -1 * self.battery.discharging_rate


    def get_generation(self, time):
        return 0

    def get_battery_charge_target(self, grid, time: int) -> float:
        return self.green_grid_AI.get_battery_target(grid, time)

    def get_graph(self):
        return self.graph_store.generate_graph(labels, config.graph_size, self.name, "Hours", "KW/KWh")
