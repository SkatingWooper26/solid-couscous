from BasicCalculator import BasicCalculator


class AdvancedCalculator(BasicCalculator):
    def __init__(self):
        super().__init__()
        
        self._operations.update({
            "%": self._modulo,
            "^": self._power
        })
        
    def _modulo(self, a: float, b: float) -> float:
        return a % b
    
    def _power(self, a: float, b: float) -> float:
        return a ** b
    
def get_float(prompt: str) -> float:
    while True:
        try:
            choice = float(input(prompt))
            return choice
        except ValueError:
            print("Please enter a valid number")
            
def get_option_from_list(prompt: str, choices: list[str]) -> str:
    while True:
        choice = input(prompt).lower().strip()
        
        if choice in choices:
            return choice
        print("Please pick a valid choice")
        
def main() -> None:
    calculator = AdvancedCalculator()
    print("Welcome to Python advanced calculator")
    
    while True:
        number_one = get_float("Enter number one: ")
        number_two = get_float("Enter number two: ")
        operator = get_option_from_list("Pick an operation (+, -, *, /, %, ^): ",
                                        calculator.get_operator_list())
        answer = calculator.operation(operator, number_one, number_two)
        
        print(f"{number_one} {operator} {number_two} = {answer}")
        
        again = get_option_from_list("Would you like to do another calculation? (y/n): ",
                                     ["y", "yes", "n", "no"])
        
        if again in ("y", "yes"):
            continue
        break
    
if __name__ == "__main__":
    main()