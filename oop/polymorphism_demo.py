import math

class Shape:
    def area(self):
        """Base method meant to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must override the area() method")

    def __str__(self):
        """Generic string for Shape objects."""
        return f"Shape()"


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of a rectangle."""
        return self.length * self.width

    def __str__(self):
        """String representation for Rectangle."""
        return f"Rectangle(length={self.length}, width={self.width})"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate area of a circle."""
        return math.pi * (self.radius ** 2)

    def __str__(self):
        """String representation for Circle."""
        return f"Circle(radius={self.radius})"
