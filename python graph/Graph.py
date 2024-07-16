from Vertex import Vertex

class Graph:
    def __init__(self, graphItems, connections=[]):
        self.vertices = []
        self.edges = []

        for index, item in enumerate(graphItems):
            self.vertices.append(Vertex(index, item.metadata, item.labels))
        
        for connection in connections:
            self.addEdge(connection[0], connection[1])

    def printAllVertices(self):
        [print(v) for v in self.vertices]

    def getVertex(self, vertexNumber: int) -> Vertex:
        return self.vertices[vertexNumber]

    def addUndirectedEdge(self, v1: int, v2: int) -> bool:
        if v1 < 0 or v1 >= len(self.vertices) or v2 < 0 or v2 >= len(self.vertices):
            print("Invalid vertex number. Edge not created")
            return False
        
        self.getVertex(v1).addAdjacency(v2)
        self.getVertex(v2).addAdjacency(v1)
        return True