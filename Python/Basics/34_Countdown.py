import time


def countdown(seconds: int) -> None:
    if seconds < 0:
        print("Please enter a positive number")
        return
    for remaining in range(seconds, 0, -1):
        print(remaining, end = "... ", flush = True)
        time.sleep(1)
    print("\nTime's up!")
    
def get_valid_seconds() -> int:
    while True:
            try:
                value = int(input("Choose an amount of seconds: "))
                if value > 0:
                    return value
                print("Please enter a valid amount of seconds")
            except ValueError:
                print("Please enter a valid amount of seconds")
    
def main() -> None:
    
    countdown(get_valid_seconds())
    
    
if __name__ == "__main__":
    main()