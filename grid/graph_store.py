from typing import TypeVar, Generic, List

import pygame
import pylab

import matplotlib

matplotlib.use("Agg")

import matplotlib.backends.backend_agg as agg

T = TypeVar('T')


class GraphStore(Generic[T]):
    """
    Will save metrics to be graphed at any point in time.
    """

    def __init__(self, labels: List[str], y_start: int = 0, step: int = 1, max_steps = 1000):
        self.x: List[List[float]] = []
        self.y: List[float] = []

        self.labels = labels

        self.counter = y_start
        self.step = step
        self.max_steps = max_steps

    def publish(self, data: T):
        self.x.append(data)

        self.counter += self.step
        self.y.append(self.counter)

    def generate_graph(self, labels_to_show: List[str], size, title, xlabel, ylabel):
        """
        Returns a surface with the graph which contains plots of the specified labels
        :param labels_to_show: the labels from this graph store that should be plotted
        :param size: the size of the graph
        :param title: the title of the graph
        :param xlabel: the xlabel of the graph
        :param ylabel: the ylabel of the graph
        :return: a surface with the graph rendered onto it
        """

        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

        fig = pylab.figure(figsize=size, dpi=100)
        plt = fig.gca()

        for i in range(len(labels_to_show)):
            data_index = self.labels.index(labels_to_show[i])
            plt.plot(self.y[-self.max_steps:], list(map(lambda e: e[data_index], self.x))[-self.max_steps:], colors[i], label=labels_to_show[i])

        plt.set_xlabel(xlabel)
        plt.set_ylabel(ylabel)
        plt.set_title(title)
        plt.legend()

        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        matplotlib.pyplot.close()

        surf = pygame.image.fromstring(raw_data, size, "RGB")
        return surf
