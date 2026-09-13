import string


def remove_punctuation(sentence):
    translation_table = str.maketrans("", "", string.punctuation)
    return sentence.translate(translation_table)

def main():
    option = input("Enter a sentence: ")
    option_without = remove_punctuation(option)
    print(f"Your sentence without punctuation is {option_without!r}")


if __name__ == "__main__":
    main()