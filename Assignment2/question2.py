import math
from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__} with area: {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


def calculate_total_area(shapes):
    """
    Calculate the total area of all shapes in the list using polymorphism.
    
    Args:
        shapes: List of Shape objects
    
    Returns:
        float: Total area of all shapes
    """
    total_area = 0.0
    for shape in shapes:
        total_area += shape.area()
    return total_area


# Alternative implementation using sum() and generator expression
def calculate_total_area_concise(shapes):
    """Concise version using sum() and generator expression"""
    return sum(shape.area() for shape in shapes)


# Demonstration
if __name__ == "__main__":
    # Create a list of different shapes
    shapes = [
        Circle(5),           # Area: π * 5² ≈ 78.54
        Rectangle(4, 6),     # Area: 4 * 6 = 24
        Triangle(3, 8),      # Area: 0.5 * 3 * 8 = 12
        Square(5),           # Area: 5 * 5 = 25
        Circle(2),           # Area: π * 2² ≈ 12.57
        Rectangle(10, 2)     # Area: 10 * 2 = 20
    ]
    
    # Display individual shapes and their areas
    print("Individual Shapes:")
    for shape in shapes:
        print(f"  {shape}")
    
    print("\n" + "="*40)
    
    # Calculate total area using polymorphism
    total_area = calculate_total_area(shapes)
    print(f"Total Area: {total_area:.2f}")
    
    # Verify with concise version
    total_area_concise = calculate_total_area_concise(shapes)
    print(f"Total Area (concise): {total_area_concise:.2f}")
    
    # Manual calculation for verification
    manual_total = (math.pi * 5**2) + (4 * 6) + (0.5 * 3 * 8) + (5 * 5) + (math.pi * 2**2) + (10 * 2)
    print(f"Manual Verification: {manual_total:.2f}")