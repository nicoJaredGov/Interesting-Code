from GraphItem import GraphItem
from Graph import Graph

class ColoredGraph(Graph):
    def __init__(
        self, 
        graphItems: list[GraphItem], 
        connections: list[tuple[str, str]] = [],
        numColors: int | None = None
    ):
        super().__init__(graphItems, connections)

        self.numColors = self.calculateChromaticNumber() if numColors is None else numColors
        self.colorUsage = {i:0 for i in range(self.numColors)}
        self.colorGroups = {i:[] for i in range(self.numColors)}

    def calculateChromaticNumber(self) -> int:
        if len(self.vertices) < 1:
            return 1
        else:
            maxDegree = max(self.vertices.values(), key=lambda v: v.getDegree())
            return maxDegree.getDegree() + 1

    def colorGraph(self):
        vertex = self.getLargestUncoloredVertex()
        while (vertex != None):
            self.setColor(vertex)
            vertex = self.getLargestUncoloredVertex()

    def colorGraphBalanced(self):
        vertex = self.getLargestUncoloredVertex()
        while (vertex != None):
            self.setColorBalanced(vertex)
            vertex = self.getLargestUncoloredVertex()

    def getLargestUncoloredVertex(self) -> str | None:
        degree = -1
        largestVertex = None
        for vertex in self.vertices.values():
            if vertex.color == -1 and vertex.getDegree() > degree:
                largestVertex = vertex.getVertexLabel()
                degree = vertex.getDegree()

        return largestVertex
    
    def setColor(self, vertexLabel: str):
        vertex = self.getVertex(vertexLabel)

        used = [0] * self.numColors
        for v in vertex.getAdjacencies():
            adjacentVertexColor = self.getVertex(v).color
            if adjacentVertexColor != -1:
                used[adjacentVertexColor] = 1
            
        for i in range(self.numColors):
            if used[i] == 0:
                vertex.color = i
                self.colorGroups[i].append(vertexLabel)    
                self.colorUsage[i] += 1
                break
    
    def setColorBalanced(self, vertexLabel: str):
        vertex = self.getVertex(vertexLabel)
        availableColors = set(range(self.numColors))

        for v in vertex.getAdjacencies():
            adjacentVertexColor = self.getVertex(v).color
            if adjacentVertexColor != -1 and adjacentVertexColor in availableColors:
                availableColors.remove(adjacentVertexColor)

        if len(availableColors) == 0:
            availableColors = set(range(self.numColors))

        availableColorUsage = [(c, self.colorUsage[c]) for c in availableColors]
        color = min(availableColorUsage, key=lambda x: x[1])[0]

        vertex.color = color
        self.colorGroups[color].append(vertexLabel)        
        self.colorUsage[color] += 1
    
    def printColorGroups(self):
        for color in self.colorGroups:
            print(color,'\n')
            for v in self.colorGroups[color]:
                vertex = self.getVertex(v)
                print('  ', vertex.metadata, vertex.labels, '\n')