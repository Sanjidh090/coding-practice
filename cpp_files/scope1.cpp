// :: operator example

#include <iostream>
using namespace std;

int m = 10; // global m

int main() {
    int m = 20; // here m is local to main
    {
        int k = m;
    
        int m = 30; // here m is local to inner block
        cout << " m " << m << endl;
        cout << " :: m " << ::m << endl;
    }

    cout << "\nWe are in outer block\n";
    cout << "m = " << m << endl;  // m here is 20, the main's local m
    cout << "::m = " << ::m << endl;  // ::m still accesses the global m, which is 10

    return 0;
}
