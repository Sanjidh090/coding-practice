#include <iostream>
using namespace std;
class Square{
    private:
    double x;
    public:
    Square(double a){
        x = a ;
    }
    //setter
    void setx(double a){
        x = a;
    }
    // getter
    double getx()
    {
        return x;
    }
    //calculation
     double area() 
     {
        return x*x;
     }
};

int main(){
    Square s(5.0);
    cout << " Side :" << s.getx() << endl;
    cout << " Area :" << s.area() << endl;
    s.setx(4.0);
    cout << " New Side :" << s.getx() << endl;
    cout <<" New Area :" << s.area() << endl;
}