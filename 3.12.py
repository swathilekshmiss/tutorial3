import tkinter as tk
def string_to_uppercase():
    def convert():
        result_var.set(input_entry.get().upper())
    root = tk.Tk()
    root.title("Uppercase Converter")
    tk.Label(root, text="Enter String:").pack()
    input_entry = tk.Entry(root)
    input_entry.pack()
    result_var = tk.StringVar()
    tk.Label(root, textvariable=result_var).pack()
    tk.Button(root, text="Convert", command=convert).pack()
    root.mainloop()
