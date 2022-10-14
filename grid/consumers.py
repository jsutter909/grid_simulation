import abc
from dataclasses import dataclass
from grid.grid_market import get_scaled_time, get_solar_factor

from grid.parameters import Time


@dataclass
class Consumer(abc.ABC):

    max_consumption: float

    def get_consumption(self, time: Time) -> float:
        """
        Gets the power consumption of a consumer as a function of the time of day.
        :return: the power consumption in watts
        """
        return self.max_consumption * self._get_time_ratio(time)


    @abc.abstractmethod
    def _get_time_ratio(self, time: Time) -> float:
        """
        Gets the ratio of power consumed at the given time of day to the maximum consumption at any point in the day.
        """
        pass



class ResidentialConsumer(Consumer):

    max_consumption: float

    @abc.abstractmethod
    def _get_time_ratio(self, time: Time) -> float:
        """
        Gets the ratio of power consumed at the given time of day to the maximum consumption at any point in the day.
        """
        return 0.7 * get_scaled_time(time, Time(6, 0), Time(24, 0)) + 0.3*get_scaled_time(time, Time(17, 0), Time(20, 0))

        

@dataclass
class CommercialConsumer(Consumer):

    max_consumption: float

    @abc.abstractmethod
    def _get_time_ratio(self, time: Time) -> float:
        """
        Gets the ratio of power consumed at the given time of day to the maximum consumption at any point in the day.
        """
        pass



@dataclass
class IndustrialConsumer(Consumer):

    max_consumption: float

    @abc.abstractmethod
    def _get_time_ratio(self, time: Time) -> float:
        """
        Gets the ratio of power consumed at the given time of day to the maximum consumption at any point in the day.
        """
        return 1


