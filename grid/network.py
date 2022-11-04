from node import *

class Network :
    def __init__(self, data) :

        def createNodeList():
            nodeList = []
            for n in data:
                nodeList.append(Node(n.id, n.location, n.connections))
            return nodeList

        self.nodes = createNodeList()

    def __str__(self) :
        return ""
    
    def getNodeById(self,id):
        for n in self.nodes:
            if(n.id==id):
                return n
        return None


    







