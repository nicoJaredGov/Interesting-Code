//A simple timetable scheduler that uses graph coloring
#include "Graph.h"

//cartesian product
std::vector<Pair> findCartProduct(std::vector<std::string> v) {
    std::vector<Pair> pairs;
    int n = v.size();

    for (int i = 0; i < n; i++) {
        for (int j = i+1; j < n; j++) {
            pairs.push_back(Pair(i,j));
        }
    }

    return pairs;
            
}
//format of sharedEvents: numPairs v1 v2 v3 v4.....
//where v1 and v2 are a pair, v3 and v4 are a pair and so on
Scheduler::Scheduler(std::vector<std::string> Events, std::vector<std::string> Timeslots, std::string sharedEvents){
    events = Events;
            timeslots = Timeslots;

            graph = new Graph(events.size());

            std::stringstream input(sharedEvents);
            int num;
            input >> num;
            int event1, event2;

            for (int i=0; i<num; i++) {
                input >> event1;
                input >> event2;
                graph->addEdge(event1,event2);
            }

            graph->colorGraph();

            for (Vertex* v : graph->vertices) {
                std::cout << events[v->vertexNumber] << " : " << timeslots[v->color] << std::endl;
            }
}
