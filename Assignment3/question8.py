import random

def generate_random_numbers(count, min_val, max_val):
    """
    Generates a list of random integers within a specified range.

    Args:
        count (int): The number of random integers to generate.
        min_val (int): The minimum value for the random integers.
        max_val (int): The maximum value for the random integers.

    Returns:
        list: A list of random integers.
    """
    return [random.randint(min_val, max_val) for _ in range(count)]

def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The average of the numbers, or 0 if the list is empty.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    """
    Main function to generate random numbers, calculate their average,
    and print the results.
    """
    num_count = 10
    min_range = 1
    max_range = 100

    # Generate a list of 10 random integers between 1 and 100
    random_list = generate_random_numbers(num_count, min_range, max_range)
    print(f"Generated list: {random_list}")

    # Calculate the average of the generated numbers
    average = calculate_average(random_list)
    print(f"Average of the numbers: {average}")

if __name__ == "__main__":
    main()