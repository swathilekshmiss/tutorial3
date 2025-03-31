import tkinter as tk
import random
def computer_guesses_number():
    def new_game():
        nonlocal low, high, guess
        low, high = 1, 100
        guess = (low + high) // 2
        guess_label.config(text=f"Computer guesses: {guess}")
        for button in response_buttons:
            button.config(state=tk.NORMAL)
    def provide_hint(hint):
        nonlocal low, high, guess
        if hint == "Too small":
            low = guess + 1
        elif hint == "Too large":
            high = guess - 1
        guess = (low + high) // 2
        guess_label.config(text=f"Computer guesses: {guess}")
        if hint == "Correct":
            for button in response_buttons:
                button.config(state=tk.DISABLED)
            result_label.config(text="Correct! You won!")
    low, high = 1, 100
    guess = (low + high) // 2
    root = tk.Tk()
    root.title("Computer Guessing Game")
    guess_label = tk.Label(root, text=f"Computer guesses: {guess}")
    guess_label.pack()
    result_label = tk.Label(root, text="")
    result_label.pack()
    response_buttons = [
        tk.Button(root, text="Too small", command=lambda: provide_hint("Too small")),
        tk.Button(root, text="Too large", command=lambda: provide_hint("Too large")),
        tk.Button(root, text="Correct", command=lambda: provide_hint("Correct"))
    ]
    for button in response_buttons:
        button.pack()
    new_game_button = tk.Button(root, text="New Game", command=new_game)
    new_game_button.pack()
    root.mainloop()
