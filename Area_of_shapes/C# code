using System;

class Program
{
    static double CalculateCircleArea(double radius)
    {
        return Math.PI * Math.Pow(radius, 2);
    }

    static double CalculateRectangleArea(double length, double width)
    {
        return length * width;
    }

    static double CalculateTriangleArea(double baseLength, double height)
    {
        return 0.5 * baseLength * height;
    }

    static void Main()
    {
        Console.WriteLine("Choose a shape:");
        Console.WriteLine("1. Circle");
        Console.WriteLine("2. Rectangle");
        Console.WriteLine("3. Triangle");

        Console.Write("Enter your choice (1/2/3): ");
        int choice = int.Parse(Console.ReadLine());

        if (choice == 1)
        {
            Console.Write("Enter the radius of the circle: ");
            double radius = double.Parse(Console.ReadLine());
            double area = CalculateCircleArea(radius);
            Console.WriteLine($"The area of the circle is: {area}");
        }
        else if (choice == 2)
        {
            Console.Write("Enter the length of the rectangle: ");
            double length = double.Parse(Console.ReadLine());
            Console.Write("Enter the width of the rectangle: ");
            double width = double.Parse(Console.ReadLine());
            double area = CalculateRectangleArea(length, width);
            Console.WriteLine($"The area of the rectangle is: {area}");
        }
        else if (choice == 3)
        {
            Console.Write("Enter the base of the triangle: ");
            double baseLength = double.Parse(Console.ReadLine());
            Console.Write("Enter the height of the triangle: ");
            double height = double.Parse(Console.ReadLine());
            double area = CalculateTriangleArea(baseLength, height);
            Console.WriteLine($"The area of the triangle is: {area}");
        }
        else
        {
            Console.WriteLine("Invalid choice.");
        }
    }
}
