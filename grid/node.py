from math import sqrt


class Node :
    def __init__(self, id, location, connected):
        self.id = id
        self.connected = connected
        self.location = location

    def __str__(self) :
        def position() :
            return "Position = " + str(self.location)
        return location() + "\n"
    
