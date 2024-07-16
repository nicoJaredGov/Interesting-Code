from Vertex import Vertex

class Graph:
    def __init__(self,n):
        self.vertices = []
        self.edges = []

        #adds n new vertex objects to vertices, labelled from 0 ~ n-1
        for i in range(n):
            self.vertices.append(Vertex(i))

    #returns a vertex object corresponding to its number label
    def getVertex(self,n):
        return self.vertices[n]

    #adds an edge from v1 to v2 (directed)
    def addEdge(self,v1,v2):
        v1 = self.getVertex(v1)
        v1.addAdjacency(v2)