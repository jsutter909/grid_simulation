from typing import Tuple
import matplotlib

import config
from environment import Environment

matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import matplotlib.pyplot as plt
import matplotlib.lines as lines
from matplotlib.figure import Figure

import pylab
import colors
import pygame
from config import *

class InfoMenu:
    def __init__(self, location: Tuple[int, int], size: Tuple[int, int], env: Environment):
        self.location = location
        self.size = size
        self.env = env
        self.count=10
        


    def drawTimeBox(self,screen,time):
        r = pygame.Rect(layout['time'])
        pygame.draw.rect(screen,GRAY,r)
        font = pygame.font.SysFont(None, 48)
        s = "Time: " + str(time)
        img = font.render(s, True, colors.WHITE)
        screen.blit(img, (r.centerx-img.get_width()/2,r.centery-img.get_height()/2-30))
        s = "Day: " + str(self.env['day'][time])
        img = font.render(s, True, colors.WHITE)
        screen.blit(img, (r.centerx-img.get_width()/2,r.centery-img.get_height()/2))
        s = "Hour: " + str(int(self.env['hour'][time]))
        img = font.render(s, True, colors.WHITE)
        screen.blit(img, (r.centerx-img.get_width()/2,r.centery-img.get_height()/2+30))
    
    def drawWorldGraphBox(self,screen,grid,time):
        r = pygame.Rect(layout['worldgraph'])
        pygame.draw.rect(screen,GRAY,r)
        graph = grid.getPriceGraph()

        fig,ax = plt.subplots(3,1,figsize=(3.5,7), dpi=100,facecolor=graph_bg_color)   
        
        g = grid.price_graph_store
        data_index = g.labels.index("price")
        ax[0].plot(g.y[-g.max_steps:], list(map(lambda e: e[data_index], g.x))[-g.max_steps:], "b", label="Price($)")
        ax[0].set_xlabel("Hours")
        ax[0].set_ylabel("Dollars ($/kwH)")
        ax[0].set_title("Energy Price")
        ax[0].set_facecolor(graph_face_color)

        env=self.env

        past = time-ticks_per_day
        if(past<0):
            past=0
        ax[1].plot(env["time"][past:time],env["sun"][past:time])
        ax[1].set_xlabel("Time")
        ax[1].set_ylabel("Sun")
        ax[1].set_title("Sun Strength")
        ax[1].set_ylim(bottom=0)
        ax[2].plot(env["time"][past:time],env["wind"][past:time])
        ax[2].set_xlabel("Time")
        ax[2].set_ylabel("Wind")
        ax[2].set_title("Wind Strength")
        ax[2].set_ylim(bottom=0)

        fig.subplots_adjust(
                    #left=0.1,
                    #bottom=0.5,
                    #right=0.9,
                    #top=0.9,
                    #wspace=0.4,
                    hspace=0.8
        )
        
        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        matplotlib.pyplot.close()
        surf = pygame.image.fromstring(raw_data, size, "RGB")
        screen.blit(surf, (r.centerx-surf.get_width()/2, r.top))

    def drawLegendBox(self,screen):
        r = pygame.Rect(layout['legend'])
        pygame.draw.rect(screen,GRAY,r)
        bigfont = pygame.font.SysFont(None, 48)
        s = "Legend"
        img = bigfont.render(s, True, colors.WHITE)
        screen.blit(img, (r.centerx-img.get_width()/2,r.top+10))

        font = pygame.font.SysFont(None, 30)
        houselocation = (r.centerx-img.get_width()/2-30,r.top+60)
        pygame.draw.polygon(screen,config.theme['house'], get_regular_polygon_points(3,20,houselocation),0)
        s = "Residential House"
        img = font.render(s, True, colors.WHITE)
        screen.blit(img, (r.centerx-img.get_width()/2+25,r.top+60))

        subr = pygame.Rect(1,1,40,40)
        subr.center = (r.centerx-img.get_width()/2,r.top+120)
        pygame.draw.rect(screen,theme['substation'],subr)
        s = "Power Station"
        img = font.render(s, True, colors.WHITE)
        screen.blit(img, (r.centerx-img.get_width()/2+15,r.top+110))

        powerlocation = (r.centerx-img.get_width()/2-20,r.top+180)
        pygame.draw.circle(screen, config.theme['powerplant'], powerlocation, 20, 0)
        s = "Power Plant"
        img = font.render(s, True, colors.WHITE)
        screen.blit(img, (r.centerx-img.get_width()/2+10,r.top+170))

    
    def drawGridGraphBox(self,screen,grid,time):
        r = pygame.Rect(layout['gridgraph'])
        pygame.draw.rect(screen,GRAY,r)

        #fig = Figure(figsize=(5,10), dpi=100,facecolor=graph_bg_color)
        #axs = fig.add_subplot(3,1)
        fig,axs = plt.subplots(3,1,figsize=(5,10), dpi=100,facecolor=graph_bg_color)

        labels_to_show = ["consumption", "battery charge", "generation", "net grid flow"]
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']   
       
        xlabel = "Hours"
        ylabel = "KW/KWh"

        #for house in grid.houses:
        for i in range(len(axs)):
            ax = axs[i]
            house = grid.houses[i]
            title = house.name + " stats"
            #ax = fig.add_subplot(i+1,1,i+1)
            g = house.graph_store
            for i in range(len(labels_to_show)):
                data_index = g.labels.index(labels_to_show[i])
                ax.plot(g.y[-g.max_steps:], list(map(lambda e: e[data_index], g.x))[-g.max_steps:], colors[i], label=labels_to_show[i])
                ax.set_xlabel(xlabel)
                ax.set_ylabel(ylabel)
                ax.set_title(title)
                ax.set_facecolor(graph_face_color)
                handles, labels = ax.get_legend_handles_labels()




        
        fig.subplots_adjust(
                    #left=0.1,
                    #bottom=0.1,
                    #right=0.9,
                    #top=0.9,
                    #wspace=0.4,
                    hspace=0.8
        )
        fig.legend(handles,labels,loc='lower center',borderaxespad=0,bbox_transform=fig.transFigure)
        canvas = agg.FigureCanvasAgg(fig)

        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        matplotlib.pyplot.close()
        surf = pygame.image.fromstring(raw_data, size, "RGB")
        screen.blit(surf, (r.centerx-surf.get_width()/2, r.top-50))
        # if(self.count>=10):
        #     self.grid_graphs = grid.get_grid_graphs()
        #     self.count=0
        # self.count+=1
        # counter = 0
        # for graph in self.grid_graphs:
        #     screen.blit(graph, (r.centerx-graph.get_width()/2, r.top+counter))
        #     counter += config.graph_spacing

    def draw(self,screen,grid,time):
        self.drawTimeBox(screen,time)
        self.drawWorldGraphBox(screen,grid,time)
        self.drawLegendBox(screen)
        self.drawGridGraphBox(screen,grid,time)


    def getGraph(self,size,title,x,y,xlabel,ylabel):
        

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