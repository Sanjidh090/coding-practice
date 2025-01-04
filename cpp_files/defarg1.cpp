#include <iostream>
using namespace std;

int volume(int x)
{
    return x*x*x;
}
double volume(double r,int h)
{
    return 3.14165*r*r*h;
}
long volume (long l,long b,long h)
{
    return l*b*h;
}
int main()
{
    cout << volume(10) <<endl;
    cout << volume(10,5,3) <<endl;
    cout << volume(10,5) <<endl;
    return 0;
}
