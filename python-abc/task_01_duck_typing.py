import math
from abc import ABC, abstractmethod

# 1. Shape Abstract Class
class Shape(ABC):
    """
    Abstract base class representing a generic shape.
    Enforces subclasses to implement area and perimeter methods.
    """
    
    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


# 2. Circle and Rectangle Classes
class Circle(Shape):
    """Concrete class representing a Circle, inheriting from Shape."""
    
    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle (pi * r^2)."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter of the circle (2 * pi * r)."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete class representing a Rectangle, inheriting from Shape."""
    
    def __init__(self, width, height):
        """Initialize the rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle (width * height)."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle (2 * (width + height))."""
        return 2 * (self.width + self.height)


# 3. shape_info Function
def shape_info(shape):
    """
    Standalone function that accepts any object with area and perimeter methods.
    Demonstrates Duck Typing by executing methods without explicit type checks.
    """
    # Directly calling the methods relying on duck typing (no isinstance checks)
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")


# 4. Testing
if __name__ == "__main__":
    # Instantiate a Circle and a Rectangle
    my_circle = Circle(5)
    my_rectangle = Rectangle(4, 7)

    # Pass each object to the shape_info function
    print("--- Circle Information ---")
    shape_info(my_circle)

    print("\n--- Rectangle Information ---")
    shape_info(my_rectangle)
