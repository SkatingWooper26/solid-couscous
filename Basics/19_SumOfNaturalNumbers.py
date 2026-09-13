
def sumOfNaturalNum(n):
    return (n * (n + 1)) // 2

while True:
    try:
        number = int(input("Enter a number: "))
        
        if number <= 0:
            print("Number has to be above 0")
            continue
        
        break
    except ValueError:
        print("Has to be a whole number")
        
natNumSum = sumOfNaturalNum(number)

print(f"The sum of all natural numbers leading up to {number} is {natNumSum}")