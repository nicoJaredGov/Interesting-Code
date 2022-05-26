#include "Graph.h"

//vertex
Vertex::Vertex(int vertNum) {
    vertexNumber = vertNum;
}

void Vertex::addAdjacency(Vertex* adjacentVertex) {
    adjacencies.push_back(adjacentVertex);
}

// bool Vertex::isAdjacent(Vertex* vertex){
//     bool found = search(adjacencies.begin() != adjacencies.end(),vertex);
//     return found;
// }

void Vertex::printAdjacencies(){
     for (int i=0; i<adjacencies.size(); i++)
        std::cout << ' ' << adjacencies[i]->vertexNumber;
    
    std::cout<<std::endl;
}

int Vertex::getDegree() {
    return adjacencies.size();
}

void Vertex::setColor(int degree){
    std::vector<int> used(degree,0);
    for (Vertex* v : adjacencies) {
        if (v->color != -1)
        used[v->color] = 1;
    }

    for (int i=0; i<degree; i++) {
        if (used[i] == 0) {
            color = i;
            break;
        }
    }
}

//edge
Edge::Edge(Vertex* v1, Vertex* v2) {
    vert1 = v1;
    vert2 = v2;
}

void Edge::setWeight(int newWeight){
    weight = newWeight;
}

//undirected graph
Graph::Graph(int n){
    for (int i=0; i<n; i++) vertices.push_back(new Vertex(i));
}

Vertex* Graph::getVertex(int n) {
    return vertices.at(n);
}

void Graph::addEdge(int v1, int v2) {
    getVertex(v1)->addAdjacency(getVertex(v2));
    getVertex(v2)->addAdjacency(getVertex(v1));
}

int Graph::getBiggestVertex(){
    int degree = -1;
    int biggestNum = -1;
    Vertex* curr = nullptr;

    for (int i=0; i<vertices.size(); i++) {
        curr = vertices[i];
        if (curr->getDegree() > degree && curr->color == -1) {
            biggestNum = curr->vertexNumber;
            degree = curr->getDegree();
        }
    }

    return biggestNum;
}

void Graph::colorGraph(){
    int big = getBiggestVertex();
    int graphDegree = vertices.size();
    while (big != -1) {
        vertices[big]->setColor(graphDegree);
        big = getBiggestVertex();
    }
}

void Graph::dfs(Vertex* v) {
    v->isInTree = true;
    for (Vertex* d : v->adjacencies) {
        if (!d->isInTree) {
            d->parent = v->vertexNumber;
            dfs(d);
        }
    }
}

// spec(ification) format: degree numEdges v1 v2 v3 v4 .... put edges between two pairs of vertices
Graph* makeGraph(std::string spec){
    int degree, numEdges;
    int vertexA, vertexB;
    std::stringstream input(spec);

    //make graph
    input >> degree;
    Graph* graph = new Graph(degree);

    //add edges
    input >> numEdges;
    for (int i=0; i<numEdges; i++){
        input >> vertexA;
        input >> vertexB;
        graph->addEdge(vertexA,vertexB);
    }

    return graph;
}
