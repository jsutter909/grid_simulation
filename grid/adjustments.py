
import abc
from dataclasses import dataclass
from typing import List, Tuple

from config import ticks_per_day

class ConsumptionAdjustment(abc.ABC):

    def get_consumption_adjustment(self, time) -> float:
        ...

    def get_day_graph(self) -> Tuple[List[int], List[float]]:

        x_axis = list(range(ticks_per_day))
        y_axis = [self.get_consumption_adjustment(time) for time in x_axis]

        return (x_axis, y_axis)


@dataclass
class ChargingCarAdjustment(ConsumptionAdjustment):

    charging_rate: float
    charging_time: int # numticks

    def get_consumption_adjustment(self, time: int) -> float:
        normalized_time = time // ticks_per_day

        start_time = round(165*(17.5/24)) #start charging at 5:30 pm

        if start_time <= normalized_time <= start_time + self.charging_time:
            return self.charging_rate
        else:
            return 0



