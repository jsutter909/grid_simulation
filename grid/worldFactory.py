from typing import List, Tuple , Optional
import enum
from house import *
from substation import *
from powerline import *
from powerplant import *
from world import *



class WorldFactory:
  def getWorld():
    data = {
      "houses":[
        House(1,(400, 300),"Bobs house", Generator.solar),
        House(2,(400, 400),"Johns house", Generator.solar),
        House(3,(400, 500),"Kims house", Generator.solar),
      ],
      "substations":[
        Substation(1,(500,400),[1,2,3],[],[2]),
        Substation(2,(600,400),[],[1,2],[1]),
      ],
      "powerplants":[
        PowerPlant(1,"Coal",(700,300),10,100,10),
        PowerPlant(2,"Gas",(700,500),50,200,10),
      ]
    }
    return World(data)
