import abc
import math
from dataclasses import dataclass
from grid.grid_market import get_solar_factor

from grid.parameters import Time, Weather, PowerRange


class Producer(abc.ABC):

    @abc.abstractmethod
    def get_power_range(self, weather: Weather, time: Time) -> PowerRange:
        ...


@dataclass
class WindPlant(Producer):

    capacity: float

    def get_power_range(self, weather: Weather, time: Time) -> PowerRange:
        return PowerRange(min_power=0, max_power=self.capacity*weather.wind)


@dataclass
class SolarPlant(Producer):

    capacity: float

    def get_power_range(self, weather: Weather, time: Time) -> PowerRange:
        return PowerRange(
            min_power=0, max_power=self.capacity * weather.cloud_cover * get_solar_factor(time)
        )
