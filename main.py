# Define a base class for all shapes
class Shape:
    def __init__(self, name):
        self._name = name

    def area(self):
        raise NotImplementedError("Subclasses must implement area method")

    def perimeter (self):
        raise NotImplementedError("Subclasses must implement perimeter method")

    def __str__(self):
        return f"{self._name}"



class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self._radius = radius

    def area(self):
        return 3.14 * (self._radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self._radius


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)


class Square(Rectangle):
    def __init__(self, name, side_length):
        super().__init__(name, side_length, side_length)


shapes = [
    Circle("Circle", 5),
    Rectangle("Rectangle", 4, 6),
    Square("Square", 3)
]


for shape in shapes:
    print(f"{shape}: area={shape.area():.2f}, perimeter={shape.perimeter():.2f}")