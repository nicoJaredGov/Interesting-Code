class Vertex:
    def __init__(self,n):
        self.vertexNumber = n
        self.adjacencies = []
        self.color = -1
        self.parent = -1
        self.isInTree = False

    def addAdjacency(self,v):
        self.adjacencies.append(v)

    def isAdjacent(self,v):
        return v in self.adjacencies

    def getDegree(self):
        return len(self.adjacencies)
    