
def celsiusToFahrenheit(celsius):
    return (celsius * 1.8) + 32

def fahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

choice = input("Do you want to convert CELSIUS or FAHRENHEIT? (C/F): ").strip().lower()

if choice == "c":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsiusToFahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")
elif choice == "f":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheitToCelsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius}°C")
else:
    print("Invalid choice. Please enter 'C' for Celsius or 'F' for Fahrenheit.")