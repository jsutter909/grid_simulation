from typing import List, Tuple , Optional
import enum
from dataclasses import dataclass

from network import *
class Generator(enum.Enum): 
  solar = 'solar'
  wind = 'wind'


@dataclass
class Node:
    id: int
    location: Tuple[int, int]
    connections: List[int]

@dataclass
class House(Node):
  name: str
  generatorType: Optional[Generator]

@dataclass
class Substation(Node):
  name: str


class gridFactory:
    def getNetwork():
      data = [
        House(1,(400, 300),[4],"Bobs house", Generator.solar),
        House(2,(400, 400),[4],"Johns house", Generator.solar),
        House(3,(400, 500),[4],"Kims house", Generator.solar),
        Substation(4,(500, 400),[1,2,3],"Main"),
      ]
      return Network(data)