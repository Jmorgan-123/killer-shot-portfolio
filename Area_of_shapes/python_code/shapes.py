import math


class Rectangle:
    def __init__(self):
        self.__len = 0
        self.__wid = 0

    def get_length(self):
        return self.__len

    def get_width(self):
        return self.__wid

    def get_area(self):
        return self.__len * self.__wid

    def get_perimeter(self):
        return 2 * (self.__len + self.__wid)

    def set_values(self):
        length = float(input("Enter the length:\t"))
        width = float(input("Enter the width:\t"))
        self.__len = length
        self.__wid = width


class Circle:
    def __init__(self):
        self.__rad = 0

    def get_radius(self):
        return self.__rad

    def get_area(self):
        return math.pi * self.__rad**2

    def get_perimeter(self):
        return 2 * math.pi * self.__rad

    def set_values(self):
        radius = float(input("Enter radius: "))
        self.__rad = radius


class Triangle:
    def __init__(self):
        self.__b = 0
        self.__h = 0

    def get_base(self):
        return self.__b

    def get_height(self):
        return self.__h

    def get_area(self):
        return (1 / 2.0) * self.__b * self.__h

    def set_values(self):
        base = float(input("Enter base size: "))
        height = float(input("Enter height size: "))
        self.__b = base
        self.__h = height


class Square:
    def __init__(self):
        self.__s = 0

    def get_side(self):
        return self.__s

    def get_area(self):
        return self.__s ** 2

    def get_perimeter(self):
        return 4 * self.__s

    def set_values(self):
        side = float(input('Enter size of side: '))
        self.__s = side
