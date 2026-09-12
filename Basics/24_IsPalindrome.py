
def is_palindrome(word):
    cleaned = word.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def main():
    entry = input("Enter a string: ")
    
    if is_palindrome(entry):
        print(f"{entry!r} is a palindrome")
    else:
        print(f"{entry!r} is not a palindrome")

if __name__ == "__main__":
    main()