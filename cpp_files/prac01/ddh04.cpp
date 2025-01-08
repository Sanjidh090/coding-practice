#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main() {
    string line;
    ifstream read("Hellow90.txt");  // Open the file

    // Use a for loop to read lines from the file
    for (; getline(read, line); ) {
        cout << line << endl;  // Output the read line
    }

    read.close();  // Close the file
    return 0;
}
