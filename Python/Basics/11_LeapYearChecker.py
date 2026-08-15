
def CheckLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True
        elif year % 100 != 0:
            return True
        else:
            return False
    else:
        return False
    
number = int(input("Enter a year: "))

if CheckLeapYear(number):
    print(f"The year {number} is a leap year")
else:
    print(f"The year {number} is not a leap year")
