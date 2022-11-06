from dataclasses import dataclass
from typing import List

from grid_componenets.house import House
from grid_componenets.powerplant import PowerPlant
from grid_componenets.substation import Substation

@dataclass
class GridConfiguration:

    houses: List[House]
    power_plants: List[PowerPlant]

    substation: Substation

