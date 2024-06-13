import tkinter as tk
from functools import partial

def button_click(entry, text):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + text)

# Function to clear the entry box
def clear(entry):
    entry.delete(0, tk.END)

# Function to evaluate the expression in the entry box
def evaluate(entry):
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def create_calculator():
    # Create the main window
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("300x400")

    # Create an entry widget for the display
    entry = tk.Entry(root, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
    entry.grid(row=0, column=0, columnspan=4)

    # Button labels
    button_labels = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+'
    ]

    row_val = 1
    col_val = 0
    for label in button_labels:
        if label == "=":
            btn = tk.Button(root, text=label, padx=20, pady=20, font=("Arial", 18),command=partial(evaluate,entry))
        else:
            btn = tk.Button(root, text=label, padx=20, pady=20, font=("Arial", 18),command=partial(button_click,entry, label))
        
        btn.grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    # Clear button
    clear_button = tk.Button(root, text='C', padx=20, pady=20, font=("Arial", 18), command=partial(clear,entry))
    clear_button.grid(row=row_val, column=0, columnspan=4)

    # Run the application
    root.mainloop()

# Run the calculator application
create_calculator()
