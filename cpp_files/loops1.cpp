#include <iostream>
using namespace std;
int main(){
    int n;
    cout << "Enter the number ";
    cin >> n  ;
    printf("%d",n);
    for(int i=1;i<=10;i++)
    {
        cout << n << "*" << i << " = " << n*i << endl;
    }
    return 0;
}