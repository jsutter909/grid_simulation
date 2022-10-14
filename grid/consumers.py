import abc

from grid.parameters import Time


class Consumer(abc.ABC):

    @abc.abstractmethod
    def get_consumption(self, time: Time) -> float:
        """
        Gets the power consumption of a consumer as a function of the time of day.
        :return: the power consumption in watts
        """
        pass


class ResidentialConsumer(Consumer):

    def get_consumption(self, time: Time) -> float:
        pass


class CommercialConsumer(Consumer):

    def get_consumption(self, time: Time) -> float:
        pass


class IndustrialConsumer(Consumer):

    def get_consumption(self, time: Time) -> float:
        pass

