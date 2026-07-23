class Vertex:
    def __init__(self, vertexLabel: str, metadata={}, labels={}):
        self.__vertexLabel = vertexLabel
        self.__adjacencies: set[str] = set()
        self.color = -1
        self.labels = labels
        self.metadata = metadata

    def getVertexLabel(self) -> str:
        return self.__vertexLabel
    
    def getDegree(self) -> int:
        return len(self.__adjacencies)

    def getAdjacencies(self) -> set[str]:
        return self.__adjacencies

    def addAdjacency(self, vertexLabel: str):
        self.__adjacencies.add(vertexLabel)

    def isAdjacent(self, vertexLabel: str) -> bool:
        return vertexLabel in self.__adjacencies

    def __repr__(self) -> str:
        repr = f'vertex {self.__vertexLabel} - '
        repr += f'metadata:{self.metadata}\t\t'
        repr += f'labels:{self.labels}\t\t'
        repr += f'color:{self.color}\t'
        repr += f'adjacencies:{self.__adjacencies}'
        return repr
    