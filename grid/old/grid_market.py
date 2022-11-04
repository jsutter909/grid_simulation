

import math
from grid.parameters import Time


SOLAR_START_TIME = Time(6, 0)
SOLAR_END_TIME = Time(18, 0)

def get_scaled_time(time: Time, begin_time: Time, end_time: Time) -> float:
    """
    Gets the time scaled to be between 0 and 1.
    :param time: the time to scale
    :param begin_time: the beginning of the time range
    :param end_time: the end of the time range
    :return: the scaled time
    """
    return math.sin((time.time_to_minutes() - begin_time.time_to_minutes()) / (end_time.time_to_minutes() - begin_time.time_to_minutes()))

def get_solar_factor(time: Time) -> float:
    """
    Computes intensity of solar power on a location given the time of day.
    :param time The time of day
    :return: The intensity of the solar power
    """
    return get_scaled_time(time, SOLAR_START_TIME, SOLAR_END_TIME)
