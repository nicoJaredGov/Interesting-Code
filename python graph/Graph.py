from Vertex import Vertex
from GraphItem import GraphItem
from itertools import groupby, combinations

class Graph:
    def __init__(
        self, 
        graphItems: list[GraphItem], 
        connections: list[tuple[str, str]] = []
    ):
        self.vertices: dict[str, Vertex] = {}

        for item in graphItems:
            self.vertices[item.vertexLabel] = Vertex(**vars(item))
        
        for connection in connections:
            self.addUndirectedEdge(connection[0], connection[1])

    def printAllVertices(self):
        [print(v) for v in self.vertices]
        print("\n")

    def getVertex(self, vertextLabel: str) -> Vertex:
        return self.vertices[vertextLabel]

    def addDirectedEdge(self, start: str, end: str):
        self.getVertex(start).addAdjacency(end)
        
    def addUndirectedEdge(self, v1: str, v2: str):
        self.getVertex(v1).addAdjacency(v2)
        self.getVertex(v2).addAdjacency(v1)
    
    def connectByLabels(self, label):
        labelAccessor = lambda x: x.labels[label]

        for _, group in groupby(sorted(self.vertices.values(), key=labelAccessor), labelAccessor):
            for (v1, v2) in combinations(group, 2):
                self.addUndirectedEdge(v1.getVertexLabel(), v2.getVertexLabel())