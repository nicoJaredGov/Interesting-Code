class Vertex:
    def __init__(self, vertexNumber, metadata={}, labels={}):
        self.__vertexNumber = vertexNumber
        self.__adjacencies = set()
        self.color = -1
        self.labels = labels
        self.metadata = metadata

    def getVertexNumber(self):
        return self.__vertexNumber
    
    def getDegree(self):
        return len(self.__adjacencies)

    def getAdjacencies(self):
        return self.__adjacencies

    def addAdjacency(self, vertexNumber):
        self.__adjacencies.add(vertexNumber)

    def isAdjacent(self, vertexNumber):
        return vertexNumber in self.__adjacencies

    def __repr__(self) -> str:
        repr = f'vertex {self.__vertexNumber} - '
        repr += f'metadata:{self.metadata}\t\t'
        repr += f'labels:{self.labels}\t\t'
        repr += f'color:{self.color}\t'
        repr += f'adjacencies:{self.__adjacencies}'
        return repr
    