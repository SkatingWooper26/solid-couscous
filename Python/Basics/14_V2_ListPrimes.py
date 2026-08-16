
def listPrimes(num):
    
    if num <= 2:
        return []
    isPrime = [True] * num
    isPrime[0] = isPrime[1] = False
    
    for i in range(2, int(num**0.5) + 1):
        if isPrime[i]:
            for j in range(i*i, num, i):
                isPrime[j] = False
    
    return [i for i, prime in enumerate(isPrime) if prime]

number = int(input("Enter a number: "))

primes = listPrimes(number)

print(f"The primes before the number {number} are", *primes)