#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main()
{
    string line;
    ifstream read;
    read.open("Hellow90.txt");
    while(getline(read,line)){
       cout << line << endl;
    }
    read.close();
    return 0;
}
