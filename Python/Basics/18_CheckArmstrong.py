
def isArmstrong(number):
    if number < 0:
        return False
    
    digits = str(number)
    total = 0
    
    for digit in digits:
        total += int(digit) ** len(digits)
        
    return total == number

while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Please enter a whole number")
        
if isArmstrong(num):
    print(f"The number {num} is an Armstrong number")
else:
    print(f"The number {num} is not an Armstrong number.")