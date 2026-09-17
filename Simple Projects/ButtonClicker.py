import tkinter as tk

def change(num):
    global money
    money += num
    my_string_var.set(f"{money}")


main = tk.Tk()
main.title("Window")
main.geometry("200x200")

money = 0
click_power = 1
my_string_var = tk.StringVar()
my_string_var.set(money)

my_label = tk.Label(main, textvariable=my_string_var, width=10).grid(column=0, padx = 55, pady = 10)
my_button_one = tk.Button(main, text="change", command= lambda:change(click_power), width=10).grid(column=0, row=1)
my_button_two = tk.Button(main, text="change x2", command= lambda:change(click_power*2), width=10).grid(column=0, row=2)
main.mainloop()