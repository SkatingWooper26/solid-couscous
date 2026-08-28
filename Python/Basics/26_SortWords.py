

def sort_words(sentence):
    words = sentence.split()
    return sorted(words, key = str.lower)

def main():
    text = input("Enter a sentance: ")
    words_sorted = sort_words(text)
    
    print(f"We sorted the sentence {text!r} into their seperate words: \n",
          *words_sorted)
    

if __name__ == "__main__":
    main()