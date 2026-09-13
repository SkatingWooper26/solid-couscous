
def generateMultTable(num):
    return [num*i for i in range(1,13)]

number = int(input("Enter a number: "))

multTable = generateMultTable(number)

print(f"The multiplication table for {number} is\n", *multTable)