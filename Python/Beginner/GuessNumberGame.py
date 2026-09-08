import random


def get_choice(
    question: str, 
    answers: list[str]
) -> str:
    answers_in_string = ", ".join(answers)
    full_question = f"{question} ({answers_in_string}): "
    
    while True:
        answer = input(full_question).lower()
        
        if answer in answers:
            break
        print("Please enter one of the options")
    return answer

def get_positive_int(
    question: str, 
    minimum: int = 1,
    maximum: int | None = None
) -> int:
    while True:
        try:
            result = int(input(question))
        except ValueError:
            print("Please enter a whole number")
        
        if result < minimum:
            print(f"Please enter a number above {minimum}")
            continue
        
        if maximum is not None and result > maximum:
            print(f"Please enter a number below {maximum}")
            continue
        
        return result

def guess_number(
    min_number:int = 1, 
    max_number:int = 100
) -> None:
    target = random.randint(min_number, max_number)
    guess = 0
    attempts = 0
    
    while True:
        attempts += 1
        guess = get_positive_int(
            f"Please guess a number between {min_number} and {max_number}: ",
            minimum = min_number,
            maximum = max_number)

        if guess == target:
            print(f"You guessed the number {target}!")
            break
        elif guess < target:
            print(f"The number {guess} is too low!")
        elif guess > target:
            print(f"The number {guess} is too high!")
        else:
            print("There seems to be an error")
    print(f"It took {attempts} guesses!")

def play_levels(levels: list[int]) -> None:
    for index, level in enumerate(levels, start=1):
        print(f"Level {index}")
        guess_number(max_number=level)

def main() -> None:
    modes = {
        "easy": (10, 20, 50, 100, 250),
        "medium": (25, 50, 100, 250, 500),
        "hard": (100, 500, 1000, 2500, 10000),
        "custom": "N/A"
    }
    
    while True:
        modes_keys = list(modes.keys())
        mode = get_choice("Pick a difficulty", modes_keys)
        
        if mode == "custom":
            lower_bound = get_positive_int("Please enter the lower bound: ")
            upper_bound = get_positive_int("Please enter the upper bound: ")
            if lower_bound > upper_bound:
                lower_bound, upper_bound = upper_bound, lower_bound
            guess_number(lower_bound, upper_bound)
        else:
            play_levels(levels = modes[mode])
            
        again = get_choice("Want to play again?", ("y", "n"))
        if again != "y":
            break
    
    

if __name__ == "__main__":
    main()