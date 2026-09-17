import tkinter as tk

def print_name():
    fn = fn_entry.get().strip()
    ln = ln_entry.get().strip()
    
    if fn == "" and ln == "":
        error_message.set("Please enter first and last name")
    elif fn == "":
        error_message.set("Please enter first name")
    elif ln == "":
        error_message.set("Please enter last name")
    else:
        error_message.set("Nothing bad happened")
        print(f"Hello {fn.capitalize()} {ln.lower()}!")

root = tk.Tk()
root.geometry("380x200")
root.title("Name entry")

fn_label = tk.Label(root, text="Enter your first name:")
fn_label.grid(row=0, column=0, padx=10, pady=5)

ln_label = tk.Label(root, text="Enter your last name:")
ln_label.grid(row=1, column=0, padx=10, pady=5)

fn_entry = tk.Entry(root)
fn_entry.grid(row=0, column=1)

ln_entry = tk.Entry(root)
ln_entry.grid(row=1, column=1)

button = tk.Button(root, text="Validate Name", command=print_name)
button.grid(row=4, column=0, pady=15, padx=40)

error_message = tk.StringVar()
error_message.set("")

error_label = tk.Label(root, textvariable=error_message, fg="red")
error_label.grid(row=3, column=0)

root.mainloop()

