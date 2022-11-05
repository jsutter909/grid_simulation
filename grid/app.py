
from dataclasses import dataclass


class App:

    def __init__(self, grid, info_menu, is_menu_open = False):

        self.grid = grid
        self.info_menu = info_menu
        self.info_menu_open = is_menu_open

    def update(self,time):
        self.grid.update(time)

    def draw(self,screen):
        self.grid.draw(screen)
        self.info_menu.draw(screen,self.grid)