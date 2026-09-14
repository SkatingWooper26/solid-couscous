from pathlib import PosixPath
import json
import random

LEADERBOARD_PATH = PosixPath(__file__).resolve().parent / "Leaderboards.json"


def save_leaderboards(data: dict) -> None:
    with LEADERBOARD_PATH.open("w", encoding="utf-8") as leaderboards:
        json.dump(data, leaderboards, indent=4)

def get_leaderboards(wanted_difficulty: str | None = None) -> dict:
    with LEADERBOARD_PATH.open(encoding = "utf-8") as f:
        leaderboard_data = json.load(f)
    
    if wanted_difficulty is not None:
        return leaderboard_data[wanted_difficulty]
    else:
        return leaderboard_data
        
def update_leaderboards(name: str, difficulty: str, score: int) -> None:
    leaderboard_data = get_leaderboards()
        
    if difficulty not in leaderboard_data:
        leaderboard_data[difficulty] = {}
        
    if name not in leaderboard_data[difficulty]:
        leaderboard_data[difficulty][name] = score
    elif leaderboard_data[difficulty][name] < score:
        leaderboard_data[difficulty].update({name:score})

    save_leaderboards(leaderboard_data)

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
            continue
        
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
) -> int:
    target = random.randint(min_number, max_number)
    guess = 0
    attempts = 0
    
    current_score = 0
    max_score = (max_number - min_number) * 10
    
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
    current_score = attempts * 5
    final_score = max(0, max_score - current_score)
    print(f"Your final score was {final_score}")
    return final_score


def play_levels(levels: list[int]) -> int:
    total_score = 0
    for index, level in enumerate(levels, start=1):
        print(f"Level {index}")
        total_score += guess_number(max_number=level)
    return total_score

def main() -> None:
    modes = {
        "easy": (10, 20, 50, 100, 250),
        "medium": (25, 50, 100, 250, 500),
        "hard": (100, 500, 1000, 2500, 10000),
        "custom": "N/A"
    }
    name = input("Please enter a username: ").lower()
    
    while True:
        modes_keys = list(modes.keys())
        mode = get_choice("Pick a difficulty", modes_keys)
        
        if mode == "custom":
            lower_bound = get_positive_int("Please enter the lower bound: ")
            upper_bound = get_positive_int("Please enter the upper bound: ")
            if lower_bound > upper_bound:
                lower_bound, upper_bound = upper_bound, lower_bound
            final_score = guess_number(lower_bound, upper_bound)
        else:
            final_score = play_levels(levels = modes[mode])
        
        update_leaderboards(name, mode, final_score)
        print(f"{name}'s final score was {final_score}")
        
        again = get_choice("Want to play again?", ("y", "n"))
        if again != "y":
            break
    
    

if __name__ == "__main__":
    main()