

class BasicCalculator:
    def __init__(self):
        self._operations = {
            "+": self._add,
            "-": self._subtract,
            "*": self._multiply,
            "/": self._divide
        }
    
    def get_operator_list(self) -> tuple[str, ...]:
        return tuple(self._operations.keys())
    
    def _add(self, a: float, b: float) -> float:
        return a + b
    
    def _subtract(self, a: float, b: float) -> float:
        return a - b
    
    def _multiply(self, a: float, b: float) -> float:
        return a * b
    
    def _divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("You can't divide by zero")
        return a / b
    
    def operation(self, choice: str, num1: float, num2: float) -> float:
        operator = self._operations.get(choice)
        
        if operator is None:
            raise ValueError(f"Unsupported operator: {choice}")
        
        return operator(num1, num2)

def get_choice_from_list(prompt: str, choices: list[str]) -> str:
    while True:
        user_choice = input(prompt).lower().strip()
        
        if user_choice not in choices:
            print("Please choose from", *choices)
            continue
        
        return user_choice
    
def get_valid_float(prompt: str) -> float:
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Please enter a valid number")

def main() -> None:
    calculator = BasicCalculator()
    print("Welcome to the Python Basic Calculator")
    
    while True:
        number_one = get_valid_float("Enter number one: ")
        number_two = get_valid_float("Enter number two: ")
        chosen_operator = get_choice_from_list("Please pick an operation (+, -, *, /): ",
                                               calculator.get_operator_list())
        
        try:
            answer = calculator.operation(chosen_operator, number_one, number_two)
        except ZeroDivisionError as error:
            print(error)
            continue
        
        print(f"{number_one} {chosen_operator} {number_two} = {answer}")
        
        again_bool = get_choice_from_list("Want to do another calculation? (y, n): ",
                                          ["y", "yes", "n", "no"])
        
        if again_bool in ("y", "yes"):
            continue
        break
    
if __name__ == "__main__":
    main()