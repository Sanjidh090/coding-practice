/* C++ Program to Show Counter using Constructor  */

#include<iostream>
using namespace std;

class counter
{
    private:
        int count;
    public:
        counter ()        // constructor
        {
            count=6;
        }

        void inc_count ()
        {
            count++;
        }

        int get_count ()
        {
            return count;
        }
};

int main ()
{
    counter c1;
    cout<<"\nBefore calling Counter Function, Count = ";
    cout<<c1.get_count ();

    c1.inc_count ();
    cout<<"\n\nAfter calling Counter Function, Count = ";
    cout<<c1.get_count ();

    cout<<"\n";

    return 0;
}