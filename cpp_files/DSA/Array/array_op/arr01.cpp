#include <iostream>
using namespace std;

int main() {
    // Creating an array of DVD names with fixed size
    const int size = 15;
    string dvds[size] = {};  // Initialize all elements to empty string

    // Writing items into the array
    dvds[7] = "The Avengers";  // 8th place, index 7
    dvds[3] = "The Incredibles";
    dvds[3] = "Star Wars";  // Overwrites The Incredibles

    // Reading items from an array
    cout << dvds[3] << endl;  // Outputs "Star Wars"
    if (dvds[10] == "  ss ")
        cout << "null" << endl; 
    else cout << "ddd" << endl; // Outputs null for empty strings

    // Writing items with a loop
    int squares[10];  // Array of 10 integers
    for (int i = 0; i < 10; ++i) {
        squares[i] = i * i;  // Store square numbers
    }

    // Reading items with a loop
    for (int i = 0; i < 10; ++i) {
        cout << squares[i] << endl;  // Outputs each square number
    }

    // Using a for loop to print non-empty DVD slots
    for (int i = 0; i < size; ++i) {
        if (dvds[i] != "") {
            cout << dvds[i] << endl;  // Outputs non-empty DVD names
        }
    }

    return 0;
}
