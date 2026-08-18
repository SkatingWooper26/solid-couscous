import math

def isPrime(num):
    if num<= 1:
        return False
    
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    
    return True

number = int(input("Enter a number: "))

if isPrime(number):
    print(f"The number {number} is prime")
else:
    print(f"The number {number} is not prime")