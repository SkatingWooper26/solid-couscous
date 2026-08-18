import math

def listPrimes(num):
    result = []
    
    for i in range(2, num):
        isPrime = True
        
        for number in range(2, int(math.sqrt(i)) + 1):
            if i % number == 0:
                isPrime = False
                break
        
        if isPrime:
            result.append(i)
        
    return result
    
number = int(input("Enter a number: "))

primes = listPrimes(number)

print(f"The primes before the number {number} are", *primes)