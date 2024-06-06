# Function to convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert temperature from Celsius to Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Get user input for temperature and unit
temperature = float(input("Enter the temperature value: "))
unit = input("Enter the unit of measurement (Celsius, Fahrenheit, or Kelvin): ")

if unit.lower() == 'celsius':
    # Convert Celsius to Fahrenheit and Kelvin
    fahrenheit = celsius_to_fahrenheit(temperature)
    kelvin = celsius_to_kelvin(temperature)
    print(f"{temperature} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit and {kelvin} Kelvin.")
elif unit.lower() == 'fahrenheit':
    # Convert Fahrenheit to Celsius and Kelvin
    celsius = (temperature - 32) * 5/9
    kelvin = celsius_to_kelvin(celsius)
    print(f"{temperature} degrees Fahrenheit is equal to {celsius} degrees Celsius and {kelvin} Kelvin.")
elif unit.lower() == 'kelvin':
    # Convert Kelvin to Celsius and Fahrenheit
    celsius = temperature - 273.15
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{temperature} Kelvin is equal to {celsius} degrees Celsius and {fahrenheit} Fahrenheit.")
else:
    print("Invalid unit of measurement. Please enter Celsius, Fahrenheit, or Kelvin.")23