
def HCF(a, b):
    
    a = abs(a)
    b = abs(b)
    
    while b != 0:
        
        a, b = b, a % b
        
    return a

def main():

    numbers = []
    
    for prompt in ("Enter the first number: ", "Enter the second number: "):
        while True:
            try:
                numbers.append(int(input(prompt)))
                break
            except ValueError:
                print("Please enter a whole number")
                
    num1, num2 = numbers
    hcf = HCF(num1, num2)
    
    print(f"The highest common factor of {num1} and {num2} is {hcf}")
    
if __name__ == "__main__":
    main()