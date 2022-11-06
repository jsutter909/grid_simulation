from typing import Tuple
import matplotlib

from environment import Environment

matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import pylab
import colors
import pygame
from config import ticksperday

class InfoMenu:
    def __init__(self, location: Tuple[int, int], size: Tuple[int, int], env: Environment):
        self.location = location
        self.size = size
        self.env = env

    def drawWorldInfo(self,env,screen):
        s = "Time: " + str(env['time'][-1])  # + " Day: " + str(self.day) + " Hour: " + str(self.hour) + " Sun Power: " + str(self.sun)
        font = pygame.font.SysFont(None, 48)
        img = font.render(s, True, colors.WHITE)
        screen.blit(img, (20, 20))

    def drawSunGraph(self,env,screen):
        surf = self.getGraph([5,2.5],"Sun Power",env["time"][-ticksperday:],env["sun"][-ticksperday:],"Time","Sun Power")
        screen.blit(surf, self.location + (500, 0))

    def getGraph(self,size,title,x,y,xlabel,ylabel):
        fig = pylab.figure(figsize=size, dpi=100)
        plt = fig.gca()
        plt.plot(x, y)
        plt.set_xlabel(xlabel)
        plt.set_ylabel(ylabel)
        plt.set_title(title)
        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        matplotlib.pyplot.close()
        surf = pygame.image.fromstring(raw_data, size, "RGB")
        return surf

    def draw(self,screen,grid,time):
        self.drawWorldInfo(self.env,screen)
        self.drawSunGraph(self.env,screen)

    # def draw_surface_loads_curves(self, n_hours_to_display_top_loadplot, n_hours_to_display_bottom_loadplot):
    #     # Loads curve surface: retrieve images surfaces, stack them into a common surface, plot horizontal lines
    #     # at top and bottom of latter surface
    #
    #     # compute the string number of days
    #     n_days_horizon = n_hours_to_display_top_loadplot // 24
    #     img_loads_curve_week = self.create_plot_loads_curve(
    #         n_timesteps=int(n_hours_to_display_top_loadplot * 3600 // self.timestep_duration_seconds),
    #         left_xlabel=' {} day{} ago  '.format(n_days_horizon, 's' if n_days_horizon > 1 else ''))
    #     n_hours_horizon = n_hours_to_display_bottom_loadplot
    #     img_loads_curve_day = self.create_plot_loads_curve(
    #         n_timesteps=int(n_hours_to_display_bottom_loadplot * 3600 // self.timestep_duration_seconds),
    #         left_xlabel='{} hours ago'.format(n_hours_horizon))
    #     loads_curve_surface = pygame.Surface(
    #         (img_loads_curve_week.get_width(), 2 * img_loads_curve_week.get_height() + 30),
    #         pygame.SRCALPHA, 32).convert_alpha()
    #     loads_curve_surface.fill(self.left_menu_tile_color)
    #     loads_curve_surface.blit(self.bold_white_render('Historical total consumption'), (30, 10))
    #     loads_curve_surface.blit(img_loads_curve_week, (0, 30))
    #     loads_curve_surface.blit(img_loads_curve_day, (0, 30 + img_loads_curve_week.get_height()))
    #     gfxdraw.hline(loads_curve_surface, 0, loads_curve_surface.get_width(), 0, (64, 64, 64))
    #     gfxdraw.hline(loads_curve_surface, 0, loads_curve_surface.get_width(), loads_curve_surface.get_height() - 1,
    #                   (64, 64, 64))
    #
    #     return loads_curve_surface
    #
    # def create_plot_loads_curve(self, n_timesteps, left_xlabel):
    #     facecolor_asfloat = np.asarray(self.left_menu_tile_color) / 255.
    #     layout_config = {'pad': 0.2}
    #     fig = pylab.figure(figsize=[3, 1.5], dpi=100, facecolor=facecolor_asfloat, tight_layout=layout_config)
    #     ax = fig.gca()
    #     # Retrieve data for the specified time
    #     data = np.sum(self.loads, axis=-1)
    #     data = data[-min(len(data), n_timesteps):]
    #     n_data = len(data)
    #     ax.plot(np.linspace(n_data, 0, num=n_data), data, '#d24dff')
    #     # Ticks and labels
    #     ax.set_xlim([n_timesteps, 1])
    #     ax.set_xticks([1, n_timesteps])
    #     ax.set_xticklabels(['now', left_xlabel])
    #     ax.set_ylim([0, np.max(data) * 1.05])
    #     ax.set_yticks([0, np.max(data)])
    #     ax.set_yticklabels(['', '%.0f MW' % (np.max(data))])
    #     label_color_hexa = '#D2D2D2'
    #     ax.tick_params(axis='y', labelsize=6, pad=-30, labelcolor=label_color_hexa, direction='in')
    #     ax.tick_params(axis='x', labelsize=6, labelcolor=label_color_hexa)
    #     # Top and right axis
    #     ax.spines['right'].set_visible(False)
    #     ax.spines['top'].set_visible(False)
    #
    #     ax.set_facecolor(np.asarray(self.background_color) / 255.)
    #     fig.tight_layout()
    #
    #     canvas = agg.FigureCanvasAgg(fig)
    #     canvas.draw()
    #     renderer = canvas.get_renderer()
    #     raw_data = renderer.tostring_rgb()
    #     size = canvas.get_width_height()
    #
    #     return pygame.image.fromstring(raw_data, size, "RGB")