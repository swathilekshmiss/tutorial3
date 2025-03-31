import tkinter as tk
def string_to_uppercase():
    root = tk.Tk()
    root.title("Uppercase Converter")
    entry, output_label = tk.Entry(root), tk.Label(root, text="")
    entry.pack(), tk.Button(root, text="Convert", command=lambda: output_label.config(text=entry.get().upper())).pack()
    output_label.pack()
    root.mainloop()
