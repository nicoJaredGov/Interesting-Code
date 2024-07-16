from Vertex import Vertex
from GraphItem import GraphItem

class Graph:
    def __init__(self, graphItems: list[GraphItem], numColors: int | None = None, connections = []):
        self.vertices: list[Vertex] = []
        self.edges = []
        self.numColors = len(graphItems) if numColors is None else numColors
        self.colourUsage = {i:0 for i in range(numColors)} 

        for index, item in enumerate(graphItems):
            self.vertices.append(Vertex(index, item.metadata, item.labels))
        
        for connection in connections:
            self.addUndirectedEdge(connection[0], connection[1])

    def printAllVertices(self):
        [print(v) for v in self.vertices]

    def getVertex(self, vertexNumber: int) -> Vertex:
        return self.vertices[vertexNumber]

    def addUndirectedEdge(self, v1: int, v2: int) -> bool:
        if v1 < 0 or v1 >= len(self.vertices) or v2 < 0 or v2 >= len(self.vertices):
            print("Invalid vertex number. Edge not created")
            return False
        
        if v1 == v2:
            print("Cannot create an edge from a vertex to itself in this model")
            return False
        
        self.getVertex(v1).addAdjacency(v2)
        self.getVertex(v2).addAdjacency(v1)
        return True
    
    #Graph coloring
    def setColor(self, vertexNumber):
        vertex = self.getVertex(vertexNumber)

        used = [0] * self.numColors
        for v in vertex.adjacencies:
            adjacentVertexColor = self.getVertex(v).color
            if adjacentVertexColor != -1:
                used[adjacentVertexColor] = 1
            
        for i in range(self.numColors):
            if used[i] == 0:
                vertex.color = i
                self.colourUsage[i] += 1
                break
    
    def setColorBalanced(self, vertexNumber):
        vertex = self.getVertex(vertexNumber)
        available = set(range(self.numColors))

        for v in vertex.adjacencies:
            adjacentVertexColor = self.getVertex(v).color
            if adjacentVertexColor != -1:
                available.remove(adjacentVertexColor)

        colorChoice = available.pop()
        minUsage = self.colourUsage[colorChoice]
        for color in available:
            usage = self.colourUsage[color]
            if usage <= minUsage:
                minUsage = usage
                colorChoice = color

        vertex.color = colorChoice        
        self.colourUsage[colorChoice] += 1
    
    def getBiggestVertexUncolored(self):
        degree = -1
        biggestVertexNumber = -1

        for vertex in self.vertices:
            if vertex.color == -1 and vertex.getDegree() > degree:
                biggestVertexNumber = vertex.vertexNumber
                degree = vertex.getDegree()
        
        return biggestVertexNumber
    
    def colorWholeGraph(self):
        big = self.getBiggestVertexUncolored()
        while (big != -1):
            self.setColor(big)
            big = self.getBiggestVertexUncolored()
    
    def colorGraphBalanced(self):
        big = self.getBiggestVertexUncolored()
        while (big != -1):
            self.setColorBalanced(big)
            big = self.getBiggestVertexUncolored()