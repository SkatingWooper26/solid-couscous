
def normalise(text):
    return "".join(sorted(ch for ch in text.lower() if ch.isalnum()))

def are_anagrams(string_one, string_two):
    string_one = normalise(string_one)
    string_two = normalise(string_two)
    return string_one == string_two

def main():
    first_string = input("Please enter the first string: ")
    second_string = input("Please enter the second string: ")
    if are_anagrams(first_string, second_string):
        print(f"{first_string!r} and {second_string!r} are anagrams")
    else:
         print(f"{first_string!r} and {second_string!r} are not anagrams")
         

if __name__ == "__main__":
    main()
    