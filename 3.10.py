import tkinter as tk
import math
def calculate_bounce_distance():
    def calculate():
        try:
            height = float(entry_height.get())
            bounciness = float(entry_bounciness.get())
            bounces = int(entry_bounces.get())
            total_distance = height
            for _ in range(bounces):
                height *= bounciness
                total_distance += 2 * height
            result_var.set(f"Total Distance: {total_distance:.2f} units")
        except ValueError:
            messagebox.showerror("Error", "Enter valid numbers")
    root = tk.Tk()
    root.title("Bouncy Ball Distance")
    tk.Label(root, text="Initial Height").pack()
    entry_height = tk.Entry(root)
    entry_height.pack()
    tk.Label(root, text="Bounciness Index").pack()
    entry_bounciness = tk.Entry(root)
    entry_bounciness.pack()
    tk.Label(root, text="Number of Bounces").pack()
    entry_bounces = tk.Entry(root)
    entry_bounces.pack()
    result_var = tk.StringVar()
    tk.Label(root, textvariable=result_var).pack()
    tk.Button(root, text="Calculate", command=calculate).pack()
    root.mainloop()
