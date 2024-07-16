from Vertex import Vertex
from GraphItem import GraphItem
from itertools import groupby, combinations

class Graph:
    def __init__(self, graphItems: list[GraphItem], numColors: int | None = None, connections = [], splitLabels: list[str] = []):
        self.vertices: list[Vertex] = []
        self.edges = []
        self.numColors = len(graphItems) if numColors is None else numColors
        self.colorUsage = {i:0 for i in range(numColors)}
        self.colorGroups = {i:[] for i in range(numColors)}
        self.splitLabels = splitLabels 

        for index, item in enumerate(graphItems):
            self.vertices.append(Vertex(index, item.metadata, item.labels))
        
        for connection in connections:
            self.addUndirectedEdge(connection[0], connection[1])

    def printAllVertices(self):
        [print(v) for v in self.vertices]
        print("\n")

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
    
    def connectByLabels(self):
        for label in self.splitLabels:
            for key, group in groupby(sorted(self.vertices, key=lambda x: x.labels[label]), lambda x: x.labels[label]):
                if key == 0 or key == False:
                    continue
                for pair in combinations(list(group),2):
                    self.addUndirectedEdge(pair[0].vertexNumber, pair[1].vertexNumber)

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
                self.colorGroups[i].append(vertex.vertexNumber)    
                self.colorUsage[i] += 1
                break
    
    def setColorBalanced(self, vertexNumber):
        vertex = self.getVertex(vertexNumber)
        available = set(range(self.numColors))

        for v in vertex.adjacencies:
            adjacentVertexColor = self.getVertex(v).color
            if adjacentVertexColor != -1:
                available.remove(adjacentVertexColor)

        colorChoice = available.pop()
        minUsage = self.colorUsage[colorChoice]
        for color in available:
            usage = self.colorUsage[color]
            if usage <= minUsage:
                minUsage = usage
                colorChoice = color

        vertex.color = colorChoice
        self.colorGroups[colorChoice].append(vertex.vertexNumber)        
        self.colorUsage[colorChoice] += 1
    
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
    
    def printColorGroups(self):
        for color in self.colorGroups:
            print(color,'\n')
            for v in self.colorGroups[color]:
                vertex = self.getVertex(v)
                print('  ', vertex.metadata, vertex.labels, '\n')