#include <iostream>
#include <cmath>
using namespace std;

double calculateCircleArea(double radius) {
    return M_PI * pow(radius, 2);
}

double calculateRectangleArea(double length, double width) {
    return length * width;
}

double calculateTriangleArea(double base, double height) {
    return 0.5 * base * height;
}

int main() {
    int choice;
    cout << "Choose a shape:" << endl;
    cout << "1. Circle" << endl;
    cout << "2. Rectangle" << endl;
    cout << "3. Triangle" << endl;

    cout << "Enter your choice (1/2/3): ";
    cin >> choice;

    if (choice == 1) {
        double radius;
        cout << "Enter the radius of the circle: ";
        cin >> radius;
        double area = calculateCircleArea(radius);
        cout << "The area of the circle is: " << area << endl;
    } else if (choice == 2) {
        double length, width;
        cout << "Enter the length of the rectangle: ";
        cin >> length;
        cout << "Enter the width of the rectangle: ";
        cin >> width;
        double area = calculateRectangleArea(length, width);
        cout << "The area of the rectangle is: " << area << endl;
    } else if (choice == 3) {
        double base, height;
        cout << "Enter the base of the triangle: ";
        cin >> base;
        cout << "Enter the height of the triangle: ";
        cin >> height;
        double area = calculateTriangleArea(base, height);
        cout << "The area of the triangle is: " << area << endl;
    } else {
        cout << "Invalid choice." << endl;
    }

    return 0;
}

