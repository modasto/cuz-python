# Define a custom exception class
class NegativeNumberError(Exception):
    """Exception raised for negative numbers."""
    def __init__(self, number, message="Negative numbers are not allowed"):
        self.number = number
        self.message = message
        super().__init__(f"{self.message}: {self.number}")

# Function that raises the custom exception
def check_positive(number):
    """
    Checks if a number is positive.
    Raises NegativeNumberError if the number is negative.
    """
    if number < 0:
        raise NegativeNumberError(number)
    print(f"{number} is a positive number.")

# Demonstrate the use of the function and exception handling
if __name__ == "__main__":
    # Test with a positive number
    try:
        check_positive(10)
    except NegativeNumberError as e:
        print(f"Caught an exception: {e}")

    print("-" * 20)

    # Test with a negative number
    try:
        check_positive(-5)
    except NegativeNumberError as e:
        print(f"Caught an exception: {e}")

    print("-" * 20)

    # Test with zero
    try:
        check_positive(0)
    except NegativeNumberError as e:
        print(f"Caught an exception: {e}")