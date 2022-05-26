#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <unordered_map>

#ifndef Graph_h
#define Graph_h

struct Pair{
    int eventA;
    int eventB;

    Pair(int a, int b) {
        eventA = a;
        eventB = b;
    }
};

struct Vertex{
    int vertexNumber;
    int color = -1;
    std::vector<Vertex*> adjacencies;
    int parent = -1;
    bool isInTree = false;

    Vertex(int);
    void addAdjacency(Vertex*);
    bool isAdjacent(Vertex*);
    void printAdjacencies();
    int getDegree();
    void setColor(int);
};

struct Edge{
    Vertex* vert1;
    Vertex* vert2;
    int weight;

    Edge(Vertex*,Vertex*);
    void setWeight(int);
};

struct Graph{
    //std::vector<Edge*> edges;
    std::vector<Vertex*> vertices;

    Graph(int);
    Vertex* getVertex(int);
    void addEdge(int v1,int v2);
    int getBiggestVertex();
    void colorGraph();
    void dfs(Vertex*);
    
};

Graph* makeGraph(std::string);
std::vector<Pair> findCartProduct(std::vector<std::string>);

class Scheduler{
    std::vector<std::string> events;
    std::vector<std::string> timeslots;
    //std::vector<int> mutualEvents;
    Graph* graph;

    public:
        Scheduler(std::vector<std::string> Events, std::vector<std::string> Timeslots, std::string sharedEvents);
};

#endif