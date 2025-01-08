//Write a program that can find the roots of a quadratic equation using the concept of
//OOP//
#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    double a , b ,c ,  dis , r1 ,r2 ,real , img;
    cout << " Enter coefficients a , b , c" << endl;
    cin >> a >> b >> c ;

    dis =  b*b - 4*a*c;
    if (dis == 0)
    {
        r1 = -b/(2*a);
    }
    else if ( dis < 0)
    {
        r1 = -b/(2*a) + j*sqrt(-dis)/(2*a);
        r2 = -b/(2*a) - j*sqrt(-dis)/(2*a);
    }

    else
    {
        r1 = -b/(2*a) + j*sqrt(dis)/(2*a);
        r2 = -b/(2*a) - j*sqrt(dis)/(2*a);

    }
cout << " r1 is " << r1 << endl;
cout << "r2 is " << r2 << endl;

}
