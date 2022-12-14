import functools
import math

import config

class BatteryTargetAI:
    """
    This object, given information on the future energy price and household load, will set a target battery fill level
    as a % of full.
    """
    def __init__(self, house, env):
        self.house = house
        self.global_price_predictor = GlobalPricePredictor(env)
        self.env = env

    def get_battery_target(self, grid, time: int) -> float:

        steps = list(range(config.ticks_per_day // 2))

        price = self.global_price_predictor.predict(grid, time)

        # future_price_avg = sum(
        #     self.global_price_predictor.predict(grid, time) for time in steps
        # ) / len(steps)
        future_price_avg = config.median_power_price

        future_demand_avg = sum(
            self.house.get_non_battery_useage(time, self.env) for time in steps
        ) / len(steps)

        if future_demand_avg < 0:
            return 1

        def sigmoid(x):
            return 1.0 / (1 + math.e**(-x))

        target = sigmoid((future_price_avg / price - 1) * future_demand_avg)

        #print(f"price:{price}, future_price_avg:{future_price_avg}, future_demand_avg:{future_demand_avg}, raw_target:{future_price_avg / price * future_demand_avg}, target:{target}")

        return target

    def get_price(self, grid, time):
        return self.global_price_predictor.predict(grid, time)


class GlobalPricePredictor:
    """
    This object predicts the future price of energy
    """

    def __init__(self, env):
        self.env = env
        self.global_load_predictor = GlobalLoadPredictor(self.env)

    @functools.lru_cache
    def weekly_average_demand(self, grid) -> float:
        total_ticks = config.ticks_per_day * 7
        return sum(grid.get_homes_power(time) for time in range(total_ticks)) / total_ticks

    def predict(self, grid, time: int) -> float:
        weekly_average_power = self.weekly_average_demand(grid)
        predicted_power_demand = self.global_load_predictor.predict(grid, time)
        price_ratio = predicted_power_demand / weekly_average_power

        # power price is the ratio of current demand to average weekly demand times normal price
        return config.median_power_price * price_ratio


class GlobalLoadPredictor:
    """
    This object predicts the future load of the grid.
    """
    def __init__(self, env):
        self.env = env

    def predict(self, grid, time: int) -> float:
        return sum(house.get_non_battery_useage(time, self.env) for house in grid.houses)


class LoadPredictor:
    """
    This object predicts the future energy use of a specific household
    """
    def predict(self, house, time: int) -> float:
        return house.get_non_battery_useage(time)
