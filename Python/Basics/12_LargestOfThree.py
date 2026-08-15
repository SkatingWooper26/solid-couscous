
def largestOfThree(a, b, c):
    return max(a, b, c)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

biggestNum = largestOfThree(num1, num2, num3)

print(f"The biggest of these numbers was {biggestNum}")
