from grid_configuration import GridConfiguration
from house import *
from substation import *
from powerline import *
from powerplant import *
from grid import *


class GridFactory:

    @classmethod
    def get_grid(cls, env):
        data = GridConfiguration(
            [
                House(1, (400, 300), "Bobs house", 2, Generator.solar, []),
                House(2, (400, 400), "Johns house", 3, Generator.solar, []),
                House(3, (400, 500), "Kims house", 2, Generator.solar, []),
            ],
            [
                PowerPlant(1, "Coal", (700, 300), 10),
                PowerPlant(2, "Gas", (700, 500), 10),
            ],
            Substation(1, (500, 400), [1, 2, 3], [1, 2]),
        )
        return Grid(env, data)
