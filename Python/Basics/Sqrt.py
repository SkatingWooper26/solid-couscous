import math

def calculateSquareRoot(number):
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(number)

number = float(input("Enter a number: "))
result = calculateSquareRoot(number)
print(f"The square root of {number} is {result}")