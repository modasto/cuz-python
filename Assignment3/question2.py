def calculate_average(*args):
    """
    Calculates the average of a variable number of numerical arguments.

    This function takes any number of numerical arguments and returns their
    average. If no arguments are provided, it returns 0.

    Args:
        *args: A variable number of numerical arguments (integers or floats).

    Returns:
        float: The average of the provided numbers. Returns 0 if no arguments
               are given.
    """
    if not args:
        return 0
    
    total = sum(args)
    count = len(args)
    
    return total / count

if __name__ == '__main__':
    # Example usage of the function
    avg1 = calculate_average(1, 2, 3, 4, 5)
    print(f"The average of 1, 2, 3, 4, 5 is: {avg1}")

    avg2 = calculate_average(10, 20, 30)
    print(f"The average of 10, 20, 30 is: {avg2}")

    avg3 = calculate_average(2.5, 3.5, 4.0)
    print(f"The average of 2.5, 3.5, 4.0 is: {avg3}")

    avg4 = calculate_average()
    print(f"The average with no arguments is: {avg4}")

    # You can also pass a list or tuple by unpacking it
    numbers = [100, 200, 300, 400]
    avg5 = calculate_average(*numbers)
    print(f"The average of {numbers} is: {avg5}")