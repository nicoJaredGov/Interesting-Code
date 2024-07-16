class Vertex:
    def __init__(self, vertexNumber, metadata={}, labels={}):
        self.vertexNumber = vertexNumber
        self.adjacencies = []
        self.color = -1
        self.labels = labels
        self.metadata = metadata

    def addAdjacency(self, vertexNumber):
        self.adjacencies.append(vertexNumber)

    def isAdjacent(self, vertexNumber):
        return vertexNumber in self.adjacencies

    def getDegree(self):
        return len(self.adjacencies)
    
    def __repr__(self) -> str:
        repr = f'vertex {self.vertexNumber} - '
        repr += f'metadata:{self.metadata} \t'
        repr += f'labels:{self.labels} \t\t'
        repr += f'color:{self.color} \t'
        repr += f'adjacencies:{self.adjacencies}'
        return repr
    