from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    
    return fib(n-1) + fib(n-2)

number = int(input("Enter a number: "))

print(f"The {number} term of the fibonacci sequence is {fib(number)}")