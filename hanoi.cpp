#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <unordered_set>
#include <chrono>
#include <ctime>

using namespace std;

//TOWER OF HANOI PUZZLE - Breadth-First Search (BFS) solution//

//State refers to what the three towers look like at a given time
//The front of the string represents the bottom of the tower and back represents the top
struct State{
	string x,y,z = "";

	void show() {
		cout << "--------------------------------" << endl;
		cout << "x :" << x << endl;
		cout << "y :" << y << endl;
		cout << "z :" << z << endl;
	}
};

//Move an item from the top of on tower to another
void move(string &a, string &b) {
	char temp = a[a.length()-1];
	a.pop_back();
	b.push_back(temp);
}

//Used in conjunction with validMoves() and move() to process the move. String m is the move received from validMoves() in the BFS.
void processMove(State &s, string m) {
	if (m[0] == 'x') {
		if (m[1] == 'y') move(s.x,s.y);
		else move(s.x,s.z);
	} else if (m[0] == 'y') {
		if (m[1] == 'x') move(s.y,s.x);
		else move(s.y,s.z);
	} else {
		if (m[1] == 'x') move(s.z,s.x);
		else move(s.z,s.y);
	}
}

/*Criteria for solved: x must be empty and either y must be empty or z must be empty.
This implies that either y or z has the full stack of rings and it has
been successfully moved. This does not check the order however which is
enforced by picking only moves from validMoves() which enforces the order of rings*/

//Checks if the puzzle is solved by looking at the state.
bool isSolved(State s) {
	if (s.x.length() == 0 and (s.y.length() == 0 or s.z.length() == 0)) return true;
    else return false;
}

//Checks valid moves according to rules of the puzzle and returns a list of those possible moves
vector<string> validMoves(State s) {
	vector<string> moves;

	int tx,ty,tz;
	string x = s.x, y = s.y, z = s.z;
	
	if (x.length() == 0) tx = 10000;
	else tx = x[x.length()-1] - '0';
	if (y.length() == 0) ty = 10000;
	else ty = y[y.length()-1] - '0';
	if (z.length() == 0) tz = 10000;
	else tz = z[z.length()-1] - '0';
	
	//cout << tx << " " << ty << " " << tz << endl;
	
	if (tx < ty) {
		if (ty < tz) {
			moves.push_back("xy");
			moves.push_back("xz");
			if (y.length() != 0) moves.push_back("yz");
		} else if (tx < tz) {
			moves.push_back("xy");
			if (z.length() != 0) moves.push_back("zy");
			moves.push_back("xz");
		} else {
			moves.push_back("xy");
			if (z.length() != 0) moves.push_back("zy");
			if (z.length() != 0) moves.push_back("zx");
		}
	} else {
		if (tx < tz) {
			moves.push_back("yx");
			if (x.length() != 0) moves.push_back("xz");
			moves.push_back("yz");
		} else if (ty < tz) {
			moves.push_back("yx");
			if (z.length() != 0) moves.push_back("zx");
			moves.push_back("yz");
		} else {
			moves.push_back("yx");
			if (z.length() != 0) moves.push_back("zx");
			if (z.length() != 0) moves.push_back("zy");
		}
	}
	
	//for (string a : moves) cout << a[0] << " " << a[1] << endl;
	return moves;
	
}

//Main BFS algorithm used to solve the puzzle
void bfsSolver(State init) {
	queue<State> states;
	unordered_set<string> explored;
	
	//initialization of bfs
	states.push(init);
	State currState = init;
	currState.show();
	
	while (!states.empty()) {
		//push current state to explored/visited
        currState = states.front();
		//currState.show();             //<-uncomment to see all iterations of the BFS
        explored.insert(currState.x + "," + currState.y + "," + currState.z);

        vector<string> possibleMoves;
        bool found;

        if (isSolved(currState)) {
			cout << "Solved!" << endl;
			currState.show();
			break;
		} else {
            states.pop();
            possibleMoves = validMoves(currState); //available moves from current state
						
            for (string move : possibleMoves) {
                State nextState = currState;
                processMove(nextState,move);
                string nStatestr = nextState.x + "," + nextState.y + "," + nextState.z;

                //check if explored first before adding
                found = explored.find(nStatestr) != explored.end();
                if (!found) states.push(nextState);
            }

        }
	}
	
}

//Initialize solving for a specified number of rings on the first tower
void solveHanoi(int numRings) {
	//three columns of rings
    //x is the starting column
    State initState;
	for (int i=numRings; i>0; i--) initState.x += char(i)+'0';
	bfsSolver(initState);	
}


//Calls solveHanoi() and prints time taken (which include printing states)
int main() {
	auto start = std::chrono::system_clock::now();
	
	solveHanoi(5);
	
	auto end = std::chrono::system_clock::now();
	std::chrono::duration<double> elapsed_seconds = end-start;
	cout<<"Time taken: "<<elapsed_seconds.count()<<" seconds"<<endl;

	return 0;
}
