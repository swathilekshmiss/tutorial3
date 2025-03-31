import tkinter as tk
import math
from tkinter import messagebox
def compute_square_root():
    root = tk.Tk()
    root.title("Square Root Calculator")
    entry, result_label = tk.Entry(root), tk.Label(root, text="")
    entry.pack(), tk.Button(root, text="Calculate", command=lambda: validate_sqrt(entry, result_label)).pack()
    result_label.pack()
    root.mainloop()
def validate_sqrt(entry, label):
    try:
        num = float(entry.get())
        if num < 0:
            raise ValueError("Negative number")
        label.config(text=f"Square Root: {math.sqrt(num):.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Enter a non-negative number.")