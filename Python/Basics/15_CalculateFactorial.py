
def calculateFactorial(num):
    
    if num <= 1:
        return 1
    
    result = 1
    for i in range(2, num+1):
        result *= i
    
    return result

number = int(input("Enter a number: "))

print(f"{number}! = {calculateFactorial(number)}")