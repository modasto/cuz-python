def classify_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def main():
    while True:
        try:
            user_input = input("Enter a number (or 'q' to quit): ")
            if user_input.lower() == 'q':
                break
            number = int(user_input)
            result = classify_number(number)
            print(f"The number {number} is {result}")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()