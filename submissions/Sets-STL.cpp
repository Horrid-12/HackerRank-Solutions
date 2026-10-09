/*-----------------------------------------------------------------------

Problem Title: Sets-STL
Problem Link: /challenges/cpp-sets
Author: Horrid-12
Language: cpp

-----------------------------------------------------------------------*/



#include <iostream>
#include <set>
using namespace std;

int main() {
    int Q;
    cin >> Q;

    set<int> s;

    while (Q--) {
        int type, x;
        cin >> type >> x;

        if (type == 1) {
            s.insert(x);
        }
        else if (type == 2) {
            s.erase(x);
        }
        else if (type == 3) {
            if (s.find(x) != s.end()) {
                cout << "Yes" << endl;
            }
            else {
                cout << "No" << endl;
            }
        }
    }

    return 0;
}
