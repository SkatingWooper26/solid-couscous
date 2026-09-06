
from pathlib import Path

FILE_PATH = Path(__file__).resolve().parent / "30_FileHandling.txt"


def edit_file(text, mode):
    with FILE_PATH.open(mode, encoding="utf-8") as document:
        if mode == "a" and document.tell() > 0:
            document.write("\n")
        document.write(text)
        document.write("\n")

def read_file(specified_line):
    with FILE_PATH.open(encoding="utf-8") as document:
        content = document.readlines()
        if specified_line < 1 or specified_line > len(content):
            raise IndexError("Line number is outside the file")
        return content[specified_line - 1]
    
def ask_mode():
    modes = {"write":"w", "append":"a", "read":"r"}
    modes_keys = modes.keys()
    while True:
        choice = input("Pick to WRITE, APPEND or READ your file: ").lower()
        if choice in modes_keys:
            break
        print("Please choose from", *modes_keys)
    return modes[choice]

def main():
    mode = ask_mode()
    
    if mode != "r":
        text = input("Enter the line: ")
        edit_file(text, mode)
    else:
        while True:
            try:
                line = int(input("Pick a line to read: "))
                break
            except ValueError:
                print("Please enter a number")
        print(read_file(line), end = "")
   
        
if __name__ == "__main__":
    main()