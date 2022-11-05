import math
from typing import Dict, Union

from config import ticksperday
from grid_configuration import GridConfiguration
from house import *
from substation import *
from powerline import *
from powerplant import *
import colors


class Grid:
    def __init__(self, data: GridConfiguration):

        self.time = 0
        self.houses: List[House] = data.houses
        self.powerplants: List[PowerPlant] = data.powerplants
        self.substation: Substation = data.substation

        self.powerlines: List[PowerLine] = []

        self.environment = {
            'time': [],
            'day': [],
            'hour': [],
            'sun': [],
        }

        start = self.substation.location
        for x in self.substation.connectedHouses:
            self.powerlines.append(PowerLine(start, self.getHouseById(x).location, 1))
        for x in self.substation.connectedPowerPlants:
            self.powerlines.append(PowerLine(start, self.getPowerPlantsById(x).location, 1))

    def getHouseById(self, id):
        for n in self.houses:
            if n.id == id:
                return n
        return None

    def getPowerPlantsById(self, id):
        for n in self.powerplants:
            if n.id == id:
                return n
        return None

    # Every call of update represents a 5min time pass in game time and 1 second in real time
    # This should mean one minute of gametime equates to ~1 week of time
    def update(self):
        self.time += 1
        day = self.time // ticksperday

        hour = self.map_range(self.time % ticksperday, 0, ticksperday, 0, 24)

        mpd = 24 * 60
        minute = self.map_range(self.time % ticksperday, 0, ticksperday, 0, mpd)

        # Sun is 0 at midnight and 100 at noon
        sun = self.map_range(math.sin((((minute - (6 * 60)) % mpd) / mpd) * 2 * math.pi), -1, 1, 0, 100)

        self.environment['time'].append(self.time)
        self.environment['day'].append(day)
        self.environment['hour'].append(hour)
        self.environment['sun'].append(sun)

    def draw(self, screen):
        [x.draw(screen) for x in self.houses]
        [x.draw(screen) for x in self.powerplants]
        [x.draw(screen) for x in self.powerlines]
        self.substation.draw(screen)

    def getTotalConsumption(self):
        pass

    def GetTotalProduction(self):
        pass

    def map_range(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

    def distribute_power(self, time):

        house_power_flow: Dict[House, float] = dict()

        house_power_sinks: Dict[House, float] = dict()
        house_power_sources: Dict[House, float] = dict()
        generator_power_sources: Dict[House, float] = dict()

        for house in self.houses:
            house_useage = house.consumption_rate + sum([adj.get_consumption_adjustment(time) for adj in house.consumption_adjustments])



        requested_production = 0

