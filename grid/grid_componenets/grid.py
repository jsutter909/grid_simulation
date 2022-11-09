from typing import Dict, List

from grid_componenets.grid_configuration import GridConfiguration
from grid_componenets.house import *
from grid_componenets.substation import *
from grid_componenets.powerline import *
from grid_componenets.powerplant import *

class Grid:
    def __init__(self, env, data: GridConfiguration):
        self.houses: List[House] = data.houses
        self.power_plants: List[PowerPlant] = data.power_plants
        self.substation: Substation = data.substation

        self.power_lines: Dict[int, PowerLine] = dict()

        self.env = env

        self.price_graph_store = GraphStore(["price"], 0, config.tick_to_hour(1), config.ticks_per_day)
        self.global_price_predictor = green_grid_ai.ai.GlobalPricePredictor(self.env)

        start = self.substation.location

        for i in range(len(self.houses)):
            self.power_lines[i] = PowerLine(start, self.houses[i].location, 0)
        for i in range(len(self.power_plants)):
            self.power_lines[i + len(self.houses)] = PowerLine(start, self.power_plants[i].location, 0)

    # Every call of update represents a 5min time pass in game time and 1 second in real time
    # This should mean one minute of gametime equates to ~1 week of time
    def update(self, time: int):
        self.distribute_power(time)
        self.price_graph_store.publish((self.global_price_predictor.predict(self, time),))
        [house.update(self, time, self.env) for house in self.houses]

    def draw(self, screen):
        [x.draw(screen) for x in self.power_lines.values()]
        [x.draw(screen) for x in self.houses]
        [x.draw(screen) for x in self.power_plants]
        self.substation.draw(screen)

    def get_homes_power(self, time: int):
        return sum(house.get_non_battery_useage(time, self.env) for house in self.houses)

    def distribute_power(self, time: int):
        """
        Calculate the amount of power sent and received from each object connected to the power grid. This will also
        modify the current state of the Grid with power-lines that represent the direction and amount of flow on each
        line.
        """

        house_power_flow: List[int] = []

        for i in range(len(self.houses)):
            house = self.houses[i]
            usage = house.get_usage(self, time, self.env)
            house_power_flow.append(usage)
            self.power_lines[i].flow = usage

        total_house_usage = sum(house_power_flow)
        power_requested = -total_house_usage

        for i in range(len(self.power_plants)):
            self.power_lines[i + len(self.houses)].flow = min(power_requested/len(self.power_lines), 0)

    def get_grid_graphs(self):
        fig = pylab.figure(figsize=size,facecolor=bgcolor,dpi=100)
        
        return [house.get_graph() for house in self.houses]

    def getPriceGraph(self):
        return self.price_graph_store.generate_graph(["price"], config.graph_size, "Energy Price", "Hours", "Dollars ($/kwH)")