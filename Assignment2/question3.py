class Shape:
    def __init__(self, name="Shape"):
        self.name = name
        self.area_calculated = False  # Common initialization logic
        print(f"Initializing {self.name} - setting up area calculation framework")
    
    def calculate_area(self):
        """Base method that does nothing - meant to be overridden"""
        self.area_calculated = True
        print(f"Area calculation completed for {self.name}")
        return 0


class Rectangle(Shape):
    def __init__(self, width, height, name="Rectangle"):
        # Use super() to call the parent class constructor
        super().__init__(name)
        self.width = width
        self.height = height
        print(f"Rectangle specific initialization: {width}x{height}")
    
    def calculate_area(self):
        # First call the parent's calculate_area method using super()
        # This executes the common logic in the base class
        super().calculate_area()
        
        # Then perform the rectangle-specific area calculation
        area = self.width * self.height
        print(f"Rectangle area calculation: {self.width} * {self.height} = {area}")
        return area


class Circle(Shape):
    def __init__(self, radius, name="Circle"):
        # Call parent constructor using super()
        super().__init__(name)
        self.radius = radius
        print(f"Circle specific initialization: radius {radius}")
    
    def calculate_area(self):
        # Call parent's method for common functionality
        super().calculate_area()
        
        # Circle-specific calculation
        import math
        area = math.pi * self.radius ** 2
        print(f"Circle area calculation: π * {self.radius}² = {area:.2f}")
        return area


# Demonstration
if __name__ == "__main__":
    print("=== Creating Rectangle ===")
    rectangle = Rectangle(5, 3)
    print("\n=== Calculating Rectangle Area ===")
    rect_area = rectangle.calculate_area()
    print(f"Final Rectangle Area: {rect_area}")
    
    print("\n" + "="*40 + "\n")
    
    print("=== Creating Circle ===")
    circle = Circle(4)
    print("\n=== Calculating Circle Area ===")
    circle_area = circle.calculate_area()
    print(f"Final Circle Area: {circle_area:.2f}")
    
    print("\n" + "="*40 + "\n")
    
    # Testing polymorphism
    print("=== Polymorphism Demonstration ===")
    shapes = [Rectangle(2, 4), Circle(3)]
    
    for shape in shapes:
        print(f"\nCalculating area for {shape.name}:")
        area = shape.calculate_area()
        print(f"Area: {area:.2f}")