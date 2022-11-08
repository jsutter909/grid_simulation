from colors import *
import math

def convert_rgb(rgb):
    return tuple(x/255 for x in rgb)

ticks_per_day = 165

orb_radius = 6
orb_center_distance = 41

median_power_price = 0.10
power_slope = 2

graph_size = [5, 2.5]
graph_spacing = 250
graph_face_color = convert_rgb(LIGHTGRAY)
graph_bg_color= convert_rgb(GRAY)

def tick_to_hour(time):
    return time * 24 / ticks_per_day


theme = {
    'background':DARKGRAY,
    'house':BLUE,
    'powerplant':RED,
    'powerline':WHITE,
    'substation':BLACK
}
