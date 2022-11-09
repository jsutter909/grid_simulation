from grid_componenets.grid import Grid
from infomenu import InfoMenu


class App:

    def __init__(self, grid: Grid, info_menu: InfoMenu, is_menu_open = False):

        self.grid = grid
        self.info_menu = info_menu
        self.info_menu_open = is_menu_open

    def update(self, time):
        self.grid.update(time)

    def draw(self, screen, time):
        self.grid.draw(screen)
        self.info_menu.draw(screen, self.grid, time)