#include "Graph.h"

int main() {
    // std::string spec1 = "6 5 0 2 2 4 2 3 3 1 5 3";
    // std::string spec2 = "6 5 0 4 1 4 4 5 2 5 5 3";

    // Graph* g = makeGraph(spec2);

    // for(Vertex* v : g->vertices) {
    //     std::cout << v->vertexNumber << ": ";
    //     v->printAdjacencies();
    // }

    // // int big = g.getBiggestVertex();
    // // std::cout << big << std::endl;

    // g->colorGraph();
    // printf("\nColors: \n");
    // for(Vertex* v : g->vertices) {
    //     std::cout << v->vertexNumber << ": " << v->color << std::endl;
    // }

    // g->dfs(g->vertices[4]);
    // printf("\nParents: \n");
    // for(Vertex* v : g->vertices) {
    //     std::cout << v->vertexNumber << ": " << v->parent << std::endl;
    // }

    std::vector<std::string> Events = {"math","cam","coms","history","english","phys","actsci","stats","chem"};
    std::vector<std::string> Timeslots = {"5/11","8/11","9/11","13/11"};
    std::string sharedEvents; // = "9 1 0 2 0 3 4 0 5 6 7 8 5 1 5 1 6 1 7";

    std::getline(std::cin,sharedEvents);

    Scheduler novemberExams(Events,Timeslots,sharedEvents);

    return 0;
}