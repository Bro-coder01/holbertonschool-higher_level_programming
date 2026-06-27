from abc import ABC, abstractmethod
import math

## =========================================================================
## 1. Shape Abstract Class
## =========================================================================
class Shape(ABC):
    """
    Abstract Base Class representing a generic shape.
    Enforces the implementation of area and perimeter in subclasses.
    """
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


## =========================================================================
## 2. Concrete Classes (Circle and Rectangle)
## =========================================================================
class Circle(Shape):
    """Concrete implementation of a Circle."""
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete implementation of a Rectangle."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + height)


## =========================================================================
## 3. shape_info Function (Relying on Duck Typing)
## =========================================================================
def shape_info(shape):
    """
    Accepts an object and prints its area and perimeter.
    Does not use isinstance() checks; it trusts that the object 
    responds to .area() and .perimeter() messages (Duck Typing).
    """
    # Dynamic dispatch occurs here at runtime
    print(f"Shape: {shape.__class__.__name__}")
    print(f"  Area:      {shape.area():.2f}")
    print(f"  Perimeter: {shape.perimeter():.2f}")
    print("-" * 30)


## =========================================================================
## 4. Testing the Implementation
## =========================================================================
if __name__ == "__main__":
    # Instantiate concrete shapes
    circle_instance = Circle(radius=5)
    rectangle_instance = Rectangle(width=4, height=7)

    print("--- Displaying Shape Information ---\n")
    
    # Pass objects to the standalone function
    shape_info(circle_instance)
    shape_info(rectangle_instance)
