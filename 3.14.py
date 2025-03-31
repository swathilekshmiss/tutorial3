import tkinter as tk
from tkinter import messagebox
import math
def compute_sqrt_with_error_handling():
    def calculate():
        try:
            num = float(entry.get())
            if num < 0:
                raise ValueError("Negative number")
            result_var.set(f"{math.sqrt(num):.2f}")
        except ValueError:
            messagebox.showerror("Error", "Enter a valid non-negative number")
    root = tk.Tk()
    root.title("Square Root Calculator with Error Handling")
    tk.Label(root, text="Enter Number:").pack()
    entry = tk.Entry(root)
    entry.pack()
    result_var = tk.StringVar()
    tk.Label(root, textvariable=result_var).pack()
    tk.Button(root, text="Calculate", command=calculate).pack()
    root.mainloop()