

def count_vowels(sentence):
    sentence = sentence.lower()
    vowels = set("aeiou")
    return sum(character in vowels for character in sentence)

def main():
    text = input("Enter a sentence: ")
    vowels_in_text = count_vowels(text)
    print(f"The amount of vowels in {text!r} is {vowels_in_text}")
    

if __name__ == "__main__":
    main()