import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def user_choice(choice):
    global user_score, computer_score
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    winner = determine_winner(choice, computer_choice)
    if winner == 'user':
        user_score += 1
    elif winner == 'computer':
        computer_score += 1
    update_scores()
    show_choices(choice, computer_choice)
    show_result(winner)

def update_scores():
    label_user_score.config(text=f"Your Score: {user_score}")
    label_computer_score.config(text=f"Computer Score: {computer_score}")

def show_choices(user_choice, computer_choice):
    label_user_choice.config(text=f"Your Choice: {user_choice.capitalize()}")
    label_computer_choice.config(text=f"Computer's Choice: {computer_choice.capitalize()}")

def show_result(winner):
    if winner == 'tie':
        messagebox.showinfo("Result", "It's a tie!")
    elif winner == 'user':
        messagebox.showinfo("Result", "You win!")
    else:
        messagebox.showinfo("Result", "Computer wins!")

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")


user_score = 0
computer_score = 0

label_user_score = tk.Label(root, text=f"Your Score: {user_score}", font=('Helvetica', 12))
label_user_score.pack(pady=10)

label_computer_score = tk.Label(root, text=f"Computer Score: {computer_score}", font=('Helvetica', 12))
label_computer_score.pack()

label_user_choice = tk.Label(root, text="Your Choice: ", font=('Helvetica', 12))
label_user_choice.pack(pady=20)

label_computer_choice = tk.Label(root, text="Computer's Choice: ", font=('Helvetica', 12))
label_computer_choice.pack()

button_rock = tk.Button(root, text="Rock", width=10, command=lambda: user_choice('rock'))
button_rock.pack(pady=10)

button_paper = tk.Button(root, text="Paper", width=10, command=lambda: user_choice('paper'))
button_paper.pack(pady=10)

button_scissors = tk.Button(root, text="Scissors", width=10, command=lambda: user_choice('scissors'))
button_scissors.pack(pady=10)

root.mainloop()
