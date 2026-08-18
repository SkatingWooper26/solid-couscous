
def fib(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    
    for i in range(2, n):
        a, b = b, a + b
        
    return a + b

number = int(input("Enter a number: "))

print(f"The {number} term of the fibonacci sequence is {fib(number)}")