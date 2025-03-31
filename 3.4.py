import tkinter as tk
def temperature_converter():
    root = tk.Tk()
    root.title("Temperature Converter")
    def f_to_c():
        c_entry.delete(0, tk.END)
        c_entry.insert(0, str(round((float(f_entry.get()) - 32) * 5/9, 2)))
    def c_to_f():
        f_entry.delete(0, tk.END)
        f_entry.insert(0, str(round((float(c_entry.get()) * 9/5) + 32, 2)))
    tk.Label(root, text="Fahrenheit").grid(row=0, column=0)
    tk.Label(root, text="Celsius").grid(row=0, column=1)
    f_entry, c_entry = tk.Entry(root), tk.Entry(root)
    f_entry.grid(row=1, column=0), c_entry.grid(row=1, column=1)
    f_entry.insert(0, "32"), c_entry.insert(0, "0.0")
    tk.Button(root, text=">>>>", command=f_to_c).grid(row=2, column=0)
    tk.Button(root, text="<<<<", command=c_to_f).grid(row=2, column=1)
    root.mainloop()