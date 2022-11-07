from grid_componenets.battery import Battery
from grid_componenets.generator import SolarGenerator
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
                House((300, 200), "Bobs house", 1, Battery(20, 0, 2, 2), SolarGenerator(3.0), ()),
                House((300, 400), "Johns house", 8, Battery(20, 0, 2, 2), SolarGenerator(7.0), ()),
                House((300, 600), "Kims house", 3, Battery(10, 0, 2, 2), None, ()),
            ],
            [
                PowerPlant("Coal", (700, 300), 10),
                PowerPlant("Gas", (700, 500), 10),
            ],
            Substation((500, 400)),
        )
        return Grid(env, data)
