from Vertex import Vertex
from GraphItem import GraphItem
from itertools import groupby, combinations

class Graph:
    def __init__(self, graphItems: list[GraphItem], numColors: int | None = None, connections=[]):
        self.vertices: list[Vertex] = []
        self.edges = []
        self.numColors = len(graphItems) if numColors is None else numColors
        self.colorUsage = {i:0 for i in range(self.numColors)}
        self.colorGroups = {i:[] for i in range(self.numColors)}

        for index, item in enumerate(graphItems):
            self.vertices.append(Vertex(index, item.metadata, item.labels))
        
        for connection in connections:
            self.addUndirectedEdge(connection[0], connection[1])

    def printAllVertices(self):
        [print(v) for v in self.vertices]
        print("\n")

    def getVertex(self, vertexNumber: int) -> Vertex:
        return self.vertices[vertexNumber]

    def addUndirectedEdge(self, v1: int, v2: int):
        if v1 < 0 or v1 >= len(self.vertices) or v2 < 0 or v2 >= len(self.vertices):
            print("Invalid vertex number. Edge not created")
            return
        
        if v1 == v2:
            print("Cannot create an edge from a vertex to itself in this model")
            return
        
        self.getVertex(v1).addAdjacency(v2)
        self.getVertex(v2).addAdjacency(v1)
    
    def connectByLabels(self, label, onlyConnectTrue=True):
        for key, group in groupby(sorted(self.vertices, key=lambda x: x.labels[label]), lambda x: x.labels[label]):
            if (key == 0 or key == False) and onlyConnectTrue:
                continue
            for pair in combinations(list(group),2):
                self.addUndirectedEdge(pair[0].getVertexNumber(), pair[1].getVertexNumber())

    #Graph coloring
    def setColor(self, vertexNumber):
        vertex = self.getVertex(vertexNumber)

        used = [0] * self.numColors
        for v in vertex.getAdjacencies():
            adjacentVertexColor = self.getVertex(v).color
            if adjacentVertexColor != -1:
                used[adjacentVertexColor] = 1
            
        for i in range(self.numColors):
            if used[i] == 0:
                vertex.color = i
                self.colorGroups[i].append(vertexNumber)    
                self.colorUsage[i] += 1
                break
    
    def setColorBalanced(self, vertexNumber):
        vertex = self.getVertex(vertexNumber)
        availableColors = set(range(self.numColors))

        for v in vertex.getAdjacencies():
            adjacentVertexColor = self.getVertex(v).color
            if adjacentVertexColor != -1 and adjacentVertexColor in availableColors:
                availableColors.remove(adjacentVertexColor)

        if len(availableColors) == 0:
            availableColors = set(range(self.numColors))

        colorChoice = availableColors.pop()
        minUsage = self.colorUsage[colorChoice]
        for color in availableColors:
            usage = self.colorUsage[color]
            if usage <= minUsage:
                minUsage = usage
                colorChoice = color

        vertex.color = colorChoice
        self.colorGroups[colorChoice].append(vertexNumber)        
        self.colorUsage[colorChoice] += 1
    
    def getBiggestUncoloredVertex(self):
        degree = -1
        biggestVertexNumber = -1
        for vertex in self.vertices:
            if vertex.color == -1 and vertex.getDegree() > degree:
                biggestVertexNumber = vertex.getVertexNumber()
                degree = vertex.getDegree()

        return biggestVertexNumber
    
    def colorGraph(self, isBalanced=False):
        vertex = self.getBiggestUncoloredVertex()
        while (vertex != -1):
            if isBalanced:
                self.setColorBalanced(vertex)
            else:
                self.setColor(vertex)
            vertex = self.getBiggestUncoloredVertex()
    
    def printColorGroups(self):
        for color in self.colorGroups:
            print(color,'\n')
            for v in self.colorGroups[color]:
                vertex = self.getVertex(v)
                print('  ', vertex.metadata, vertex.labels, '\n')