#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ofstream write;
    write.open("Hellow90.txt", ios::out | ios::app);
        if (!write) {
        cerr << "Error opening file." << endl;
        return 1;
    }
    write << "KUET said HI!";
    write.close();
    return 0;
}
