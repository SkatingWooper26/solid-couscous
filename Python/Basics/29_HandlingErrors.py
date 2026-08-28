

def create_division_error():
    return 1 / 0

def create_value_error():
    return int("string")

def main():
    try:
        create_division_error()
    except ZeroDivisionError:
        print("This code caused a ZeroDivisionError")
    try:
        create_value_error()
    except ValueError:
        print("This code caused a ValueError")
    
        
if __name__ == "__main__":
    main()