#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ofstream write;
    write.open("Hellow90.txt");
        if (!write) {
        cerr << "Error opening file." << endl;
        return 1;
    }
    write << "KUET said HIy67647464y4y!";
    write.close();
    return 0;
}

