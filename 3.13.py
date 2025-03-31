import tkinter as tk
import math
def compute_sqrt_gui():
    def calculate():
        try:
            num = float(entry.get())
            result_var.set(f"{math.sqrt(num):.2f}")
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number")
    
    root = tk.Tk()
    root.title("Square Root Calculator")
    
    tk.Label(root, text="Enter Number:").pack()
    entry = tk.Entry(root)
    entry.pack()
    result_var = tk.StringVar()
    tk.Label(root, textvariable=result_var).pack()
    tk.Button(root, text="Calculate", command=calculate).pack()
    
    root.mainloop()