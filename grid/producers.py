import abc
import math
from dataclasses import dataclass

from grid.parameters import Time, Weather, PowerRange

SOLAR_START_TIME = Time(6, 0)
SOLAR_END_TIME = Time(18, 0)


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
            min_power=0, max_power=self.capacity * weather.cloud_cover * SolarPlant.get_solar_factor(time)
        )

    @classmethod
    def get_solar_factor(cls, time: Time) -> float:
        """
        Computes intensity of solar power on a location given the time of day.
        :param time The time of day
        :return: The intensity of the solar power
        """

        start_time_minutes = SOLAR_START_TIME.time_to_minutes()
        end_time_minutes = SOLAR_END_TIME.time_to_minutes()
        current_time_minutes = time.time_to_minutes()

        # will be a float in [0, 1]
        scaled_time = (current_time_minutes - start_time_minutes) / (end_time_minutes - start_time_minutes)

        return math.sin(scaled_time * math.pi)
