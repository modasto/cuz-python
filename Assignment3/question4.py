# A list of names to be written to the file
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# File path
file_path = "names.txt"

try:
    # Write the names to the file
    # The 'with' statement ensures the file is properly closed even if errors occur.
    with open(file_path, 'w') as file:
        for name in names:
            file.write(name + '\n')
    
    print(f"Successfully wrote names to {file_path}")

    print("\nReading names from the file:")
    # Read the names from the file and print them
    with open(file_path, 'r') as file:
        for line in file:
            # .strip() removes leading/trailing whitespace, including the newline character
            print(line.strip())

except IOError as e:
    print(f"An error occurred: {e}")
