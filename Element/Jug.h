#ifndef JUG_H
#define JUG_H

#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>

using namespace std;

// Helper struct to represent a state of the jugs
struct JugState {
    int amountA, amountB, cost;
    JugState *predecessor;
    string actionTaken;

    JugState(int a, int b, int c, JugState *pred = nullptr, string action = "")
        : amountA(a), amountB(b), cost(c), predecessor(pred), actionTaken(action) {}
};



class Jug {
  public:
    Jug(int Ca, int Cb, int N, int cfA, int cfB, int ceA, int ceB, int cpAB, int cpBA);
    ~Jug() {}

    // Solve the Jug problem
    int solve(string &solution);

  private:
    int capacityA, capacityB, goal;
    int costFillA, costFillB, costEmptyA, costEmptyB, costPourAB, costPourBA;

    // Validates the input parameters
    bool validateInput() const;

    // Builds and traverses the graph to find the solution
    int buildAndTraverseGraph(string &solution);
    void reconstructSolution(string &solution, JugState *goalState);
    void generateAndAddNextStates(queue<JugState> &statesQueue, map<pair<int, int>, int> &visited, const JugState &currentState);

    // Adds a state to the graph if it's a valid and new state
    void addState(queue<JugState> &states, map<pair<int, int>, int> &visited, 
                  int amountA, int amountB, int cost, string &solution);
};

#endif // JUG_H
