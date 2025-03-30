#include <iostream>
using namespace std;
//class keyword
class person
{
    char name[30];
    int age;
    //public attributes
    public:
    void getdata(void);
    void putdata(void);
//function,methods
};

void person :: getdata(void)
{
    cout << "enter name: ";
    cin >> name;
  // Insertion or put to operator/ bit-wise left-shift
    cout << "Enter age: ";
    cin >> age;
}
//:: scope resolution operator
void person :: putdata(void)
{
    cout<< "Name: " <<name;
    cout<< "\nage: " <<age;
}

int main()
{
    person p;
    p.getdata();
    p.putdata();
  //dot operator
}
