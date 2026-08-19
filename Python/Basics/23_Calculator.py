
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    else:
        return a / b

def exponent(a, b):
    return a ** b

def ask_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            break
        except ValueError:
            print("Please enter a number")
            
    return number

def ask_choices(choices):
    while True:
        print("Please choose one of the following...\n", *choices)
        choice = input("Please choose one: ").lower()
        
        if choice in choices:
            return choice

def main():
    print("Welcome to the Python Calcultor!")
    
    while True:
        print('''Please choose a calculation: 
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Exponent
        6. Exit \n''')
        
        option = ask_choices(("1", "2", "3", "4", "5", "6"))
        
        if option == "6":
            print("Bye-bye")
            break
        
        num1 = ask_number("Enter the first number: ")
        num2 = ask_number("Enter the second number: ")
        
        match option:
            case "1":
                result = add(num1, num2)
                print(f"{num1} + {num2} = {result}")
            case "2":
                result = subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")
            case "3":
                result = multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")
            case "4":
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            case "5":
                result = exponent(num1, num2)
                print(f"{num1} ^ {num2} = {result}")
                
        print("Would you like to make another calculation?")
        
        option = ask_choices(("yes", "no"))
        
        match option:
            case "yes":
                continue
            case "no":
                break

if __name__ == "__main__":
    main()