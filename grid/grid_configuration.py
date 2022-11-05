from dataclasses import dataclass
from typing import List

from house import House
from powerplant import PowerPlant
from substation import Substation

@dataclass
class GridConfiguration:

    houses: List[House]
    powerplants: List[PowerPlant]

    substation: Substation

