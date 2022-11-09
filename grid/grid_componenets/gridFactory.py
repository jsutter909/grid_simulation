from grid_componenets.battery import Battery
from grid_componenets.generator import SolarGenerator, WindGenerator
from grid_componenets.grid import Grid
from grid_componenets.grid_configuration import GridConfiguration
from grid_componenets.house import Generator, House
from grid_componenets.powerplant import PowerPlant
from grid_componenets.substation import Substation


class GridFactory:

    @classmethod
    def get_grid(cls, env):
        data = GridConfiguration(
            [
                House((600, 150), "Bobs house", 1, Battery(20, 0, 2, 2), [SolarGenerator(3.0),WindGenerator(10.0)], ()),
                House((800, 150), "Johns house", 8, Battery(20, 0, 2, 2), [SolarGenerator(7.0)], ()),
                House((1000, 150), "Kims house", 3, Battery(10, 0, 2, 2), None, ()),
            ],
            [
                PowerPlant("Coal", (700, 700), 10),
                PowerPlant("Gas", (900, 700), 10),
            ],
            Substation((800, 400)),
        )
        return Grid(env, data)
