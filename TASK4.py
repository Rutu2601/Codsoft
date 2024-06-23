import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

def generate_password():
    length = length_var.get()
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special_chars = "!@#$%^&*()"

    password = ""
    if var.get() == 1:
        # Generate a password with lowercase letters
        for _ in range(length):
            password += random.choice(characters)
    elif var.get() == 2:
        # Generate a password with uppercase letters
        for _ in range(length):
            password += random.choice(characters.upper())
    elif var.get() == 3:
        # Generate a password with digits
        for _ in range(length):
            password += random.choice(digits)
    elif var.get() == 4:
        # Generate a password with special characters
        for _ in range(length):
            password += random.choice(special_chars)
    else:
        print("Please choose an option")

    password_entry.delete(0, END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    random_password = password_entry.get()
    pyperclip.copy(random_password)

root = Tk()
root.title("Random Password Generator")

var = IntVar()
length_var = IntVar()

# GUI elements
password_label = Label(root, text="Generated Password:")
password_label.grid(row=0, column=0)

password_entry = Entry(root)
password_entry.grid(row=0, column=1)

length_label = Label(root, text="Password Length:")
length_label.grid(row=1, column=0)

length_combo = Combobox(root, textvariable=length_var, values=list(range(8, 21)))
length_combo.grid(row=1, column=1)
length_combo.current(0)

options_label = Label(root, text="Choose Character Types:")
options_label.grid(row=2, column=0)

lowercase_radio = Radiobutton(root, text="Lowercase", variable=var, value=1)
lowercase_radio.grid(row=2, column=1, sticky='W')

uppercase_radio = Radiobutton(root, text="Uppercase", variable=var, value=2)
uppercase_radio.grid(row=2, column=1, sticky='E')

digits_radio = Radiobutton(root, text="Digits", variable=var, value=3)
digits_radio.grid(row=2, column=2, sticky='W')

special_chars_radio = Radiobutton(root, text="Special Characters", variable=var, value=4)
special_chars_radio.grid(row=2, column=2, sticky='E')

generate_button = Button(root, text="Generate", command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2)

copy_button = Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=3, column=2)

root.mainloop()
