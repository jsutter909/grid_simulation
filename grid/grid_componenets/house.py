from dataclasses import dataclass
from typing import Tuple, Optional, List
import enum

import pygame

import config
import green_grid_ai.ai
from adjustments import ConsumptionAdjustment
from graph_store import GraphStore
from grid_componenets.battery import Battery

# labels = ["consumption", "target_charge", "battery_charge"]
from grid_componenets.generator import Generator
import math
labels = ["consumption", "target charge", "battery charge", "generation", "net grid flow"]

@dataclass
class House:

    location: Tuple[int, int]
    name: str
    consumption_rate: float
    battery: Battery
    generators: Optional[List[Generator]]
    consumption_adjustments: Tuple[ConsumptionAdjustment]

    def __post_init__(self):
        self.graph_store = GraphStore(labels, 0, config.tick_to_hour(1), config.ticks_per_day)
        self.points = self.get_regular_polygon_points(5,20,self.location)

    # Green grid ai here?
    def update(self, grid, time, env):
        self.graph_store.publish([
            self.get_non_battery_useage(time, env) + self.get_generation(time, env),
            self.get_battery_charge_target(grid, time, env) * self.battery.capacity,
            self.battery.charge,
            self.get_generation(time, env),
            self.get_usage(grid, time, env)])
        self.battery.charge += self.get_battery_charging(grid, time, env) * config.tick_to_hour(1)

    def consume(self):
        pass

    def produce(self):
        pass

    def draw(self, screen):      
        pygame.draw.polygon(screen,config.theme['house'],self.points,0)

    def get_non_battery_useage(self, time, env):
        return self.consumption_rate \
               - self.get_generation(time, env) \
               + sum([adj.get_consumption_adjustment(time) for adj in self.consumption_adjustments])

    def get_usage(self, grid, time, env):
        return self.get_non_battery_useage(time, env) + self.get_battery_charging(grid, time, env)

    def get_battery_charging(self, grid, time, env):
        target_charge = self.battery.capacity * self.get_battery_charge_target(grid, time, env)

        # if self.battery.charge < target_charge - self.battery.charging_rate * config.tick_to_hour(1):
        #     return self.battery.charging_rate
        # elif self.battery.charge > target_charge + self.battery.discharging_rate * config.tick_to_hour(1):
        #     return -1 * self.battery.discharging_rate
        # else:
        return target_charge - self.battery.charge

    def get_generation(self, time, env):
        generation = 0
        if not self.generators: return 0
        for g in self.generators:
            generation += g.get_generation(time, env)
        return generation

    def get_battery_charge_target(self, grid, time: int, env) -> float:
        return green_grid_ai.ai.BatteryTargetAI(self, env).get_battery_target(grid, time)

    def get_graph(self):
        return self.graph_store.generate_graph(labels, config.graph_size, self.name, "Hours", "KW/KWh")

    def get_regular_polygon_points(self,vertex_count, radius, position):
        n, r = vertex_count, radius
        x, y = position
        return [(x + r * math.cos(2 * math.pi * i / n), y + r * math.sin(2 * math.pi * i / n)) for i in range(n)]