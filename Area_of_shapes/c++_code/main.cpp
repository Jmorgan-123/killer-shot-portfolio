#include <iostream>
#include <cmath>

using namespace std;

// Function to calculate area of a circle
double areaOfCircle(double radius) {
    return M_PI * radius * radius;
}

// Function to calculate area of a rectangle
double areaOfRectangle(double length, double width) {
    return length * width;
}

// Function to calculate area of a triangle
double areaOfTriangle(double base, double height) {
    return 0.5 * base * height;
}

int main() {
    char choice;
    double radius, length, width, base, height;

    do {
        cout << "Choose a shape to calculate its area:\n";
        cout << "1. Circle\n";
        cout << "2. Rectangle\n";
        cout << "3. Triangle\n";
        cout << "Enter your choice (1-3): ";
        cin >> choice;

        switch(choice) {
            case '1':
                cout << "Enter the radius of the circle: ";
                cin >> radius;
                cout << "Area of the circle: " << areaOfCircle(radius) << endl;
                break;
            case '2':
                cout << "Enter the length of the rectangle: ";
                cin >> length;
                cout << "Enter the width of the rectangle: ";
                cin >> width;
                cout << "Area of the rectangle: " << areaOfRectangle(length, width) << endl;
                break;
            case '3':
                cout << "Enter the base of the triangle: ";
                cin >> base;
                cout << "Enter the height of the triangle: ";
                cin >> height;
                cout << "Area of the triangle: " << areaOfTriangle(base, height) << endl;
                break;
            default:
                cout << "Invalid choice! Please enter a number from 1 to 3.\n";
        }

        cout << "Do you want to calculate the area of another shape? (Y/N): ";
        cin >> choice;
    } while (choice == 'Y' || choice == 'y');

    return 0;
}
