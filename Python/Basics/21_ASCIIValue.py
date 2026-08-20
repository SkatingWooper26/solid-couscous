
def main():
    while True:
        character = input("Enter one ASCII character: ")

        if len(character) == 1 and character.isascii():
            print(f"The ASCII value of {character!r} is {ord(character)}")
            break

        print("Please enter exactly one ASCII character.")


if __name__ == "__main__":
    main()