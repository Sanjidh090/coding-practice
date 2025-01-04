#include <iostream>
#include <string>
using namespace std;
int main ()
{
int i;
cout << "Please enter an integer value: ";
cin >> i;
cout << "The value you entered is " << i;
cout <<" and its double is " << i*2 ;
string mystr;
cout <<"What's your name?";
getline (cin, mystr);
cout << "Hello" << mystr;
return 0;
}
