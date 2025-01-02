#include <iostream>
using namespace std;
class Rectangle {
private:
    double length;
    double wideth;
public:
     // constructor
     Rectangle(double I,double w){
        length = I;
        wideth = w;
     }
     //setter fir length
     double setlength(double I){
        length = I;
     }
     double getlength() {
        return length;
     }
          //setter fir length
     double setwideth(double w){
        wideth = w;
     }
     double getwideth() {
        return wideth;
     }
     //calculate area
     double area() {
        return length*wideth;
     }
};

int main(){
    Rectangle rect(10.0,5.0);

    //using public methods
    cout << "length" << rect.getlength() << endl;
    cout << "Wideth " << rect.getwideth() << endl;
    cout << "Area " << rect.area() <<endl;

    //modify attributes via setter
    rect.setlength(20.0);
    rect.setwideth(8.0);

    // printing the new values
    cout << "New length: " << rect.getlength() << endl;
    cout << "New width: " << rect.getwideth() << endl;
    cout << "New area: " << rect.area() << endl;

    return 0;
}