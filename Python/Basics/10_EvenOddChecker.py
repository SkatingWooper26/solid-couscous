
def evenOrOdd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    
number = int(input("Enter a number: "))

print(f"The number {number} is {evenOrOdd(number)}")
