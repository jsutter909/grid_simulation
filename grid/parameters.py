from dataclasses import dataclass

MINUTES_PER_HOUR = 60


@dataclass(frozen=True, kw_only=True)
class PowerRange:
    """Represents the possible range of output powers of a given type of electricity producer"""
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

    def time_to_minutes(self) -> int:
        """
        Given a time of day, return the number of minutes that have passed since midnight.
        :return: the number of minutes that have passed since midnight
        """
        return self.minute + MINUTES_PER_HOUR * self.hour
