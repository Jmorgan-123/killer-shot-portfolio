import java.util.Scanner;

public class AreaCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Choose a shape (circle, rectangle, triangle): ");
        String shape = scanner.nextLine();

        switch (shape) {
            case "circle":
                System.out.print("Enter the radius: ");
                double radius = scanner.nextDouble();
                double area = Math.PI * radius * radius;
                System.out.println("The area of the circle is: " + area);
                break;
            case "rectangle":
                System.out.print("Enter the length: ");
                double length = scanner.nextDouble();
                System.out.print("Enter the width: ");
                double width = scanner.nextDouble();
                area = length * width;
                System.out.println("The area of the rectangle is: " + area);
                break;
            case "triangle":
                System.out.print("Enter the base: ");
                double base = scanner.nextDouble();
                System.out.print("Enter the height: ");
                double height = scanner.nextDouble();
                area = 0.5 * base * height;
                System.out.println("The area of the triangle is: " + area);
                break;
            default:
                System.out.println("Invalid shape selection.");
        }
    }
}
