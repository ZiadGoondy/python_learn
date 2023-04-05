from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass


class Square(Shape):

    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return self.__side * 4


class Rect(Shape):

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__width * self.__length

    def perimeter(self):
        return 2 * (self.__width + self.__length)


square1 = Square(12)
rect1 = Rect(6, 8)

print(f" area is {square1.area()} and perimeter is {square1.perimeter()}")
print(f" area is {rect1.area()} and perimeter is {rect1.perimeter()}")
