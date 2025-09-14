class Dog:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return f"{self.name} says: Woof! Woof!"
    
    def __str__(self):
        return f"Dog named {self.name}"


class Cat:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return f"{self.name} says: Meow! Meow!"
    
    def __str__(self):
        return f"Cat named {self.name}"


class Bird:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return f"{self.name} says: Tweet! Tweet!"
    
    def __str__(self):
        return f"Bird named {self.name}"


def process_sound(sound_object):
    """
    Process any object that has a make_sound() method.
    This function doesn't need to know the specific type of the object.
    """
    print(f"Processing: {sound_object}")
    sound = sound_object.make_sound()
    print(f"Sound: {sound}")
    print(f"Sound length: {len(sound)} characters")
    print("-" * 50)
    return sound


# Alternative function that processes multiple sound objects
def process_sounds(sound_objects):
    """Process a list of objects that have make_sound() method"""
    print("=== Processing Multiple Sounds ===")
    results = []
    for obj in sound_objects:
        results.append(process_sound(obj))
    return results


# Demonstration
if __name__ == "__main__":
    # Create instances of different animals
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    bird = Bird("Tweety")
    
    # Process each animal's sound - polymorphism in action!
    print("=== Individual Sound Processing ===")
    process_sound(dog)
    process_sound(cat)
    process_sound(bird)
    
    # Process a list of different animals
    animals = [dog, cat, bird, Dog("Rex"), Cat("Mittens")]
    process_sounds(animals)
    
    # Demonstrating with unexpected object that has make_sound()
    class Car:
        def make_sound(self):
            return "Vroom! Vroom!"
        
        def __str__(self):
            return "Sports Car"
    
    car = Car()
    process_sound(car)  # This works too!