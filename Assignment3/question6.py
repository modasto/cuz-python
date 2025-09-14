def divide_numbers(numerator, denominator):
    """
    Divides two numbers and handles potential ZeroDivisionError and TypeError.

    Args:
        numerator: The number to be divided (the dividend).
        denominator: The number to divide by (the divisor).

    Returns:
        The result of the division if successful, otherwise None after
        printing an error message.
    """
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Invalid input. Please provide numbers.")

if __name__ == '__main__':
    # Example Usage
    print(f"10 / 2 = {divide_numbers(10, 2)}")
    print("-" * 20)
    print(f"10 / 0 = {divide_numbers(10, 0)}")
    print("-" * 20)
    print(f"10 / 'a' = {divide_numbers(10, 'a')}")
    print("-" * 20)
    print(f"'b' / 2 = {divide_numbers('b', 2)}")