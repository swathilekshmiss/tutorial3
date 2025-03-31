import tkinter as tk
import random
def guess_number_game():
    number, attempts = random.randint(1, 100), 0
    def check_guess():
        nonlocal attempts
        guess = int(entry.get())
        attempts += 1
        result_label.config(text="Correct!" if guess == number else "Too small!" if guess < number else "Too large!")
    root = tk.Tk()
    root.title("Guess the Number")
    entry, result_label = tk.Entry(root), tk.Label(root, text="Guess a number between 1 and 100")
    entry.pack(), tk.Button(root, text="Submit", command=check_guess).pack()
    result_label.pack()
    root.mainloop()
