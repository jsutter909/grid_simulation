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
    def __init__(self, environment, data: GridConfiguration):
        self.houses: List[House] = data.houses
        self.powerplants: List[PowerPlant] = data.powerplants
        self.substation: Substation = data.substation

        self.powerlines: List[PowerLine] = []

        self.environment = environment

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
    def update(self,time):
        pass#currentEnvironment = self.environment

    def draw(self, screen):
        [x.draw(screen) for x in self.houses]
        [x.draw(screen) for x in self.powerplants]
        [x.draw(screen) for x in self.powerlines]
        self.substation.draw(screen)

    def getTotalConsumption(self):
        pass

    def GetTotalProduction(self):
        pass


    def distribute_power(self, time):

        house_power_flow: Dict[House, float] = dict()
        powerplant_power_flow: Dict[PowerPlant, float] = dict()

        for house in self.houses:
            house_power_flow[house] = house.get_useage(time)

        total_house_usage = sum(house_power_flow.values())

        for powerplant in self.powerplants:
            powerplant_power_flow[powerplant] = min(total_house_usage)




        requested_production = 0

