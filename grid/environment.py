
from config import ticks_per_day
import math
class Environment:

    def __init__(self,timesteps):
        self.environment = {
            'time': [],
            'day': [],
            'hour': [],
            'sun': [],
            'weather': [],
        }
        time = 0
        for t in range(timesteps):
            time += 1
            day = time // ticks_per_day

            hour = self.map_range(time % ticks_per_day, 0, ticks_per_day, 0, 24)

            mpd = 24 * 60
            minute = self.map_range(time % ticks_per_day, 0, ticks_per_day, 0, mpd)

            # Sun is 0 at midnight and 100 at noon
            sun = self.map_range(math.sin((((minute - (6 * 60)) % mpd) / mpd) * 2 * math.pi), -1, 1, 0, 100)

            self.environment['time'].append(time)
            self.environment['day'].append(day)
            self.environment['hour'].append(hour)
            self.environment['sun'].append(sun)

    def __getitem__(self, index):
        return self.environment[index]


    def map_range(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
