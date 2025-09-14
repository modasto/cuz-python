# A list of temperatures in Celsius
celsius_temperatures = [0, 10, 20, 30, 37, 100]

# Use map() with a lambda function to convert Celsius to Fahrenheit
# The formula for conversion is F = C * 9/5 + 32
fahrenheit_temperatures = list(map(lambda c: c * 9/5 + 32, celsius_temperatures))

# Print the original and converted lists
print(f"Celsius temperatures: {celsius_temperatures}")
print(f"Fahrenheit temperatures: {fahrenheit_temperatures}")