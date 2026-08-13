
def celsiusToFahrenheit(celsius):
    return (celsius * 1.8) + 32

def fahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

choice = input("Do you want to convert CELSIUS or FAHRENHEIT? (C/F): ").strip().lower()

if hoice == "c":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsiusToFahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")
else:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheitToCelsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius}°C")