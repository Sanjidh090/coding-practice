#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main() {
    string line;
    ifstream read("Hellow90.txt");  // Open the file
    while(read.eof()==0){
        getline(read,line);
        cout << line << endl;
    }

    read.close();  // Close the file
    return 0;
}
