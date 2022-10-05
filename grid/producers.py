import abc
from abc import ABC
from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class PowerRange:
    min_power: float
    max_power: float


@dataclass(frozen=True, kw_only=True)
class Weather:
    # [0, 1], where 1 is max cloud cover and 0 is no cloud cover
    cloud_cover: float
    # [0, 1], where 1 is max cloud cover and 0 is no cloud covers
    wind: float


@dataclass(frozen=True, kw_only=True)
class Time:

    hour: int
    minute: int


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
        pass
        #return PowerRange(min_power=0, max_power=self.capacity*weather.cloud_cover* ##SOLAR FACTOR)

    @classmethod
    def get_solar_factor(self, time: Time):
        return #TODO: calculate the amount of sunlight
