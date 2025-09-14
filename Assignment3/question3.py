while True:
    try:
        user_input = input("Please enter a number: ")
        number = int(user_input)
        print(f"You entered the valid number: {number}")
        break  # Exit the loop if the input is a valid number
    except ValueError:
        print("Invalid input. That was not a valid number. Please try again.")
