#include <iostream>
#include <cmath>
using namespace std;

class QuadraticEquation {
private:
    double a, b, c;  // Coefficients of the equation

public:
    // Constructor to initialize the coefficients
    QuadraticEquation(double a, double b, double c) : a(a), b(b), c(c) {}

    // Method to calculate and display the roots
    void calculateRoots() {
        double discriminant = b*b - 4*a*c;
        double r1, r2; // Real parts of the root
        double imaginary; // Imaginary part of the root

        if (discriminant > 0) {
            // Two distinct real roots
            r1 = (-b + sqrt(discriminant)) / (2*a);
            r2 = (-b - sqrt(discriminant)) / (2*a);
            cout << "Roots are real and different: " << endl;
            cout << "Root 1 = " << r1 << endl;
            cout << "Root 2 = " << r2 << endl;
        } else if (discriminant == 0) {
            // One real root
            r1 = -b / (2*a);
            cout << "Root is real and single: " << endl;
            cout << "Root = " << r1 << endl;
        } else {
            //Complex roots
            r1 = -b / (2*a);
            imaginary = sqrt(-discriminant) / (2*a);
            cout << "Roots are complex: " << endl;
            cout << "Root 1 = " << r1 << " + " << imaginary << "i" << endl;
            cout << "Root 2 = " << r1 << " - " << imaginary << "i" << endl;
        }
    }
};

int main() {
    double a, b, c;
    cout << "Enter coefficients a, b, and c: ";
    cin >> a >> b >> c;
    QuadraticEquation eq(a, b, c);
    eq.calculateRoots();
    return 0;
}
