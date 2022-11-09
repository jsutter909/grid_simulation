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
    'house':LIGHTBLUE,
    'powerplant':RED,
    'powerline':WHITE,
    'substation':YELLOW,
    'text':WHITE
}

layout = {
    'time':[(30,30),(400,200)],
    'worldgraph':[(30,250),(400,800)],
    'legend':[(1120,800),(250,250)],
    'gridgraph':[(1400,30),(500,1020)],
    'simover':[(1,1),(400,100)]}


def get_regular_polygon_points(vertex_count, radius, position):
    n, r = vertex_count, radius
    x, y = position
    return [(x + r * math.cos(2 * math.pi * i / n+math.pi/2), y + r * math.sin(2 * math.pi * i / n+math.pi/2)) for i in range(n)]