

ticks_per_day = 165

orb_radius = 6
orb_center_distance = 41

median_power_price = 0.10
power_slope = 2

graph_size = [5, 2.5]
graph_spacing = 250


def tick_to_hour(time):
    return time * 24 / ticks_per_day
