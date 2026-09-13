import random

def generate_list(max_value: int, length: int) -> list[int]:
    return [random.randint(0, max_value) for _ in range(length)]

def filter_even_numbers(numbers: list[int]) -> list[int]:
    return [number for number in numbers if number % 2 == 0]

def ask_for_non_negative_int(question: str) -> int:
    while True:
        try:
            result = int(input(question))
            if result < 0:
                print("Please enter a non-negative whole number")
                continue
            return result
        except ValueError:
            print("Please enter a whole number")

def main() -> None:
    max_number = ask_for_non_negative_int("Please enter the maximum number to generate: ")
    list_length = ask_for_non_negative_int("How long should the list be: ")
    generated_list = generate_list(max_number, list_length)
    print(f"Your generated list is {generated_list!r}")
    even_numbers = filter_even_numbers(generated_list)
    print(f"The even numbers are {even_numbers!r}")


if __name__ == "__main__":
    main()