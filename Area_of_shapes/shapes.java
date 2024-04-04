import java.util.Scanner;
public class ShapeAreaCalculator {
    public static double calculateCircleArea(double radius) {
        return Math.PI * Math.pow(radius, 2);
    }
    public static double calculateRectangleArea(double length, double width) {
        return length * width;
    }
    public static double calculateTriangleArea(double base, double height) {
        return 0.5 * base * height;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Choose a shape:");
        System.out.println("1. Circle");
        System.out.println("2. Rectangle");
        System.out.println("3. Triangle");

        System.out.print("Enter your choice (1/2/3): ");
        int choice = scanner.nextInt();
        if (choice == 1) {
            System.out.print("Enter the radius of the circle: ");
            double radius = scanner.nextDouble();
            double area = calculateCircleArea(radius);
            System.out.println("The area of the circle is: " + area);
        } else if (choice == 2) {
            System.out.print("Enter the length of the rectangle: ");
            double length = scanner.nextDouble();
            System.out.print("Enter the width of the rectangle: ");
            double width = scanner.nextDouble();
            double area = calculateRectangleArea(length, width);
            System.out.println("The area of the rectangle is: " + area);
        } else if (choice == 3) {
            System.out.print("Enter the base of the triangle: ");
            double base = scanner.nextDouble();
            System.out.print("Enter the height of the triangle: ");
            double height = scanner.nextDouble();
            double area = calculateTriangleArea(base, height);
            System.out.println("The area of the triangle is: " + area);
        } else {
            System.out.println("Invalid choice.");
        }
        scanner.close();
    }
}
