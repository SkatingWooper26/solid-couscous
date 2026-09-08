import random


def get_answer_within_list(question: str, answers: list[str]) -> str:
    answer = 0
    answers_in_string = "/".join(answers)
    full_question = f"{question} ({answers_in_string}): "
    while answer not in answers:
        answer = input(full_question).lower()
        if answer not in answers:
            print("Please enter one of the options")
    return answer

def get_positive_int_above_zero(question: str) -> int:
    while True:
        try:
            result = int(input(question))
            if result <= 0:
                print("Please enter a number above zero")
                continue
            return result
        except ValueError:
            print("Please enter a number above 0")
            
def go_through_levels(levels: list[int]) -> None:
    round = 1
    for level in levels:
        print(f"Level {round}")
        guess_number(level)
        round += 1

def guess_number(max_number: int, min_number = 1) -> None:
    correct_number = random.randint(min_number, max_number)
    guessed_number = 0
    guess_amount = 0
    while guessed_number is not correct_number:
        guess_amount += 1
        guessed_number = get_positive_int_above_zero(f"Please guess the number between {min_number} and {max_number}: ")
        if guessed_number is correct_number:
            print(f"You guessed the number {correct_number}!")
        elif guessed_number < correct_number:
            print(f"The number {guessed_number} is too low!")
        elif guessed_number > correct_number:
            print(f"The number {guessed_number} is too high!")
        else:
            print("There seems to be an error")
    print(f"It took {guess_amount} guesses!")
            
def main() -> None:
    modes = {
        "easy": (10, 20, 50, 100, 250),
        "medium": (25, 50, 100, 250, 500),
        "hard": (100, 500, 1000, 2500, 10000),
        "custom": "N/A"
    }
    modes_keys = list(modes.keys())
    mode = get_answer_within_list("Pick a difficulty", modes_keys)
    if mode == "custom":
        lower_bound = get_positive_int_above_zero("Please enter the lower bound: ")
        upper_bound = get_positive_int_above_zero("Please enter the upper bound: ")
        guess_number(upper_bound, lower_bound)
    else:
        go_through_levels(modes[mode])
    choice = get_answer_within_list("Want to play again?", ("y", "n"))
    if choice == "y":
        main()
    
    

if __name__ == "__main__":
    main()