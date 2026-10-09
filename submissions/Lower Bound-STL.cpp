/*-----------------------------------------------------------------------

Problem Title: Lower Bound-STL
Problem Link: /challenges/cpp-lower-bound
Author: Horrid-12
Language: cpp

-----------------------------------------------------------------------*/



#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> v(n);
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    int q;
    cin >> q;

    while (q--) {
        int x;
        cin >> x;

        auto it = lower_bound(v.begin(), v.end(), x);
        int pos = it - v.begin();

        if (v[pos] == x) {
            cout << "Yes " << pos + 1 << endl;
        } else {
            cout << "No " << pos + 1 << endl;
        }
    }

    return 0;
}
