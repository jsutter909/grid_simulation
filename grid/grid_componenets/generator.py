import abc
from dataclasses import dataclass

import config


class Generator(abc.ABC):

    def get_generation(self, time, env):
        pass

@dataclass
class SolarGenerator(Generator):
    capacity: float

    def get_generation(self, time, env):
        return self.capacity * env["sun"][time]


@dataclass
class WindGenerator(Generator):
    capacity: float

    def get_generation(self, time, env):
        return self.capacity * env["wind"][time]
