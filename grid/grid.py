

class Grid :
    def __init__(self, data) :

        def createHouses():
            houses = []
            for n in data:
                nodeList.append(Node(n.id, n.location, n.connections))
            return nodeList

        self.houses = createNodeList()
        self.substations

    def __str__(self) :
        return ""
    
    def getNodeById(self,id):
        for n in self.nodes:
            if(n.id==id):
                return n
        return None


    