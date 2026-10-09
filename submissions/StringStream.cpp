/*-----------------------------------------------------------------------

Problem Title: StringStream
Problem Link: /challenges/c-tutorial-stringstream
Author: Horrid-12
Language: cpp

-----------------------------------------------------------------------*/



#include <iostream>
#include <sstream>
using namespace std;

int main() {
    string s;
    cin >> s;

    stringstream ss(s);
    char ch;
    int num;

    while (ss >> num) {
        cout << num << endl;
        ss >> ch;
    }

    return 0;
}
