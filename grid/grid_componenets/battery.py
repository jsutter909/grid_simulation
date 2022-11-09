
from dataclasses import dataclass

@dataclass
class Battery:
    capacity: float # unit-hours
    charge: float # unit-hours
    charging_rate: float
    discharging_rate: float

