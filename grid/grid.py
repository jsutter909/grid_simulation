import math
from house import *
from substation import *
from powerline import *
from powerplant import *
import colors




import matplotlib

matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import pylab


class Grid :
    def __init__(self, data) :

        self.time = 0
        self.houses = data['houses']
        self.substations = data['substations']
        self.powerplants = data['powerplants']
        
        self.powerlines = []

        self.environment = {
            'time':[],
            'day':[],
            'hour':[],
            'sun':[],
        }
        self.fig = pylab.figure(figsize=[4, 4], dpi=100)

        for s in self.substations:
            start = s.location
            for x in s.connectedHouses:
                self.powerlines.append(PowerLine(start,self.getHouseById(x).location))
            for x in s.connectedPowerPlants:
                self.powerlines.append(PowerLine(start,self.getPowerPlantsById(x).location))
            for x in s.connectedSubstations:
                line = PowerLine(start,self.getSubStationsById(x).location)
                for p in self.powerlines:
                    if(p.start == line.finish and p.finish == line.start):
                        break
                else:
                    self.powerlines.append(line)


    def getHouseById(self,id):
        for n in self.houses:
            if(n.id==id):
                return n
        return None

    def getSubStationsById(self,id):
        for n in self.substations:
            if(n.id==id):
                return n
        return None

    def getPowerPlantsById(self,id):
        for n in self.powerplants:
            if(n.id==id):
                return n
        return None

    #Every call of update represents a 5min time pass in game time and 1 second in real time
    #This should mean one minute of gametime equates to ~1 week of time
    def update(self):
        ticksperday = 165
        self.time+=1
        day = self.time//ticksperday

        hour = self.map_range(self.time % ticksperday, 0, ticksperday, 0, 24)

        mpd=24*60
        minute = self.map_range(self.time % ticksperday, 0, ticksperday, 0, mpd)

        #Sun is 0 at midnight and 100 at noon
        sun = self.map_range(math.sin((((minute-(6*60))%mpd)/mpd)*2*math.pi), -1, 1, 0, 100) 

        self.environment['time'].append(self.time)
        self.environment['day'].append(day)
        self.environment['hour'].append(hour)
        self.environment['sun'].append(sun)


    def draw(self,screen):
        [x.draw(screen) for x in self.houses]
        [x.draw(screen) for x in self.substations]
        [x.draw(screen) for x in self.powerplants]
        [x.draw(screen) for x in self.powerlines]
        self.drawWorldInfo(screen)
        self.drawSunGraph(screen)


    def drawWorldInfo(self,screen):
        s = "Time: " + str(self.time) #+ " Day: " + str(self.day) + " Hour: " + str(self.hour) + " Sun Power: " + str(self.sun)
        font = pygame.font.SysFont(None, 48)
        img = font.render(s, True, colors.WHITE)
        screen.blit(img, (20, 20))

    def drawSunGraph(self,screen):
        
        plt = self.fig.gca()
        plt.plot(self.environment['time'], self.environment['sun'])
        canvas = agg.FigureCanvasAgg(self.fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        surf = pygame.image.fromstring(raw_data,(400,400), "RGB")
        screen.blit(surf, (100,100))
        
    def getTotalConsumption(self):
        pass

    def GetTotalProduction(self):
        pass

    def map_range(self,x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

    
