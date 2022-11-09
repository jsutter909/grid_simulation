
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
            'wind' : []
        }
        time = 0
        for t in range(timesteps):
            time += 1
            day = time // ticks_per_day

            hour = self.map_range(time % ticks_per_day, 0, ticks_per_day, 0, 24)

            mpd = 24 * 60
            minute = self.map_range(time % ticks_per_day, 0, ticks_per_day, 0, mpd)

            weather = 0
            if(day>2 and day<4):
                weather = math.cos(self.map_range(day,2,4,-math.pi/2,math.pi/2))

            wind=self.map_range(self.windFromDay(day),0,10,0,0.75) + self.map_range(weather,0,1,0,0.25)


            # Sun is 0 at midnight and 1 at noon
            sun = self.map_range(math .sin((((minute - (6 * 60)) % mpd) / mpd) * 2 * math.pi), -1, 1, 0, 1) * (1-(weather)*.75)

            self.environment['time'].append(time)
            self.environment['day'].append(day)
            self.environment['hour'].append(hour)
            self.environment['sun'].append(sun)
            self.environment['weather'].append(weather)
            self.environment['wind'].append(wind)


    def __getitem__(self, index):
        return self.environment[index]


    def map_range(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min



    #Takes in day 0-6 and returns a value 0-10
    def windFromDay(self,day):
        x = day
        if(day<0):
            x=0
        if(day>6):
            x=6
        y = 0.02056277 + 6.179545*x - 1.827652*(x^2) - 0.8465909*(x^3) + 0.3882576*(x^4) - 0.0375*(x^5)
        if(y>10):
            return 10
        if(y<0):
            return 0
        return y