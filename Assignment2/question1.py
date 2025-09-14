class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
    
    def start_engine(self):
        return "Engine starting..."
    
    def get_type(self):
        return "Generic Vehicle"


class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors
    
    def start_engine(self):  # Method override
        return "Car engine starting with a smooth purr..."
    
    def get_type(self):  # Method override
        return "Car"
    
    def display_info(self):  # Method override with extension
        base_info = super().display_info()
        return f"{base_info} ({self.doors}-door)"


class Bike(Vehicle):
    def __init__(self, make, model, year, bike_type):
        super().__init__(make, model, year)
        self.bike_type = bike_type
    
    def start_engine(self):  # Method override
        return "Bike engine starting with a loud roar!"
    
    def get_type(self):  # Method override
        return f"{self.bike_type} Bike"
    
    def display_info(self):  # Method override with extension
        base_info = super().display_info()
        return f"{base_info} ({self.bike_type})"


# Demonstration
if __name__ == "__main__":
    # Create instances
    generic_vehicle = Vehicle("Generic", "Model", 2023)
    car = Car("Toyota", "Camry", 2022, 4)
    bike = Bike("Harley-Davidson", "Sportster", 2021, "Cruiser")
    
    # Test method overriding
    vehicles = [generic_vehicle, car, bike]
    
    print("=== Vehicle Information ===")
    for vehicle in vehicles:
        print(f"Type: {vehicle.get_type()}")
        print(f"Info: {vehicle.display_info()}")
        print(f"Start: {vehicle.start_engine()}")
        print("-" * 30)