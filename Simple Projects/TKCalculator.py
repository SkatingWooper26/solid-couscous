import tkinter as tk

expr = ""

def add(symbol: str) -> None:
    global expr, displayed_text
    
    expr += symbol
    displayed_text.set(expr)
    
def translate_expr() -> str:
    global expr
    
    table = str.maketrans("×÷", "*/")
    return expr.translate(table)
    
def equal() -> None:
    global expr, displayed_text
    try:
        answer = str(eval(translate_expr()))
        clear()
        displayed_text.set(answer)
        expr = answer
    except:
        clear()
        displayed_text.set("There was an error.")
    
def clear() -> None:
    global expr, displayed_text
    
    expr = ""
    displayed_text.set(expr)
    
def main() -> None:
    global expr, displayed_text
    
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("250x300")
    
    root.rowconfigure(tuple(range(5)), weight = 1)
    root.columnconfigure(tuple(range(4)), weight = 1)
    
    displayed_text = tk.StringVar()
    displayed_text.set(expr)
    
    display = tk.Label(textvariable = displayed_text, 
                       font= ("Fixedsys", 20),
                       relief = "sunken").grid(columnspan=4, row = 0, pady = 5, padx = 5, sticky = "nsew")
    
    buttons = (("7", 0, 1), ("8", 1, 1), ("9", 2, 1), ("+", 3, 1),
               ("4", 0, 2), ("5", 1, 2), ("6", 2, 2), ("-", 3, 2),
               ("1", 0, 3), ("2", 1, 3), ("3", 2, 3), ("×", 3, 3),
               ("C", 0, 4), ("0", 1, 4), ("=", 2, 4), ("÷", 3, 4))
    
    for sym, x, y in buttons:
        tk.Button(root, text=sym, width = 3, height = 2, font = ("Fixedsys", 10, "bold"),
                  command = lambda symbol = sym: add(symbol) if symbol not in ("=", "C") else clear() if symbol == "C" else equal()
                  ).grid(column = x, row = y, padx = 5, pady = 5, sticky = "nsew")
        
    root.mainloop()
    
if __name__ == "__main__":
    main()