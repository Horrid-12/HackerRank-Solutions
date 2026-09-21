/*-----------------------------------------------------------------------

Problem Title: Basic Data Types
Problem Link: /challenges/c-tutorial-basic-data-types
Author: Horrid-12
Language: cpp

-----------------------------------------------------------------------*/


#include <iostream>
#include <cstdio>
#include <iomanip>
using namespace std;

int main() {
    // Complete the code.
int a;
long b;
char c;
float d;
double e;
 cin >> a >> b >> c >> d >> e;
cout << a << "\n";
cout << b << "\n";
cout << c << "\n";
cout << fixed << setprecision(3) << d << "\n";
cout << fixed << setprecision(9) << e << "\n"; 
    return 0;
}
