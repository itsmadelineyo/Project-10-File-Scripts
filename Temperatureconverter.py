>>> import tkinter as tk
>>> def is_valid_number(value):
...     return value.replace(".", "", 1).isdigit() and value.count(".") <= 1
...
>>> def fahrenheit_to_celsius():
...     fahrenheit = fahrenheit_entry.get()
...     if is_valid_number(fahrenheit):
...         celsius = (float(fahrenheit) - 32) * 5/9
...         celsius_entry.delete(0, tk.END)
...         celsius_entry.insert(0, str(celsius))
...         return
...         celsius_entry.delete(0, tk.END)
...         celsius_entry.insert(0, "Invalid input")
...
>>> def celsius_to_fahrenheit():
...     celsius = celsius_entry.get()
...     if is_valid_number(celsius):
...         fahrenheit = (float(celsius) * 9/5) + 32
...         fahrenheit_entry.delete(0, tk.END)
...         fahrenheit_entry.insert(0, str(fahrenheit))
...         return
...         fahrenheit_entry.delete(0, tk.END)
...         fahrenheit_entry.insert(0, "Invalid input")
...
>>> root = tk.Tk()
>>> root.title("Temperature Converter")
''
>>> root.geometry("300x150")
''
>>> fahrenheit_label = tk.Label(root, text="Fahrenheit:")
>>> fahrenheit_label.grid(row=0, column=0, padx=5, pady=5)
>>> fahrenheit_entry = tk.Entry(root)
>>> fahrenheit_entry.grid(row=1, column=0, padx=5, pady=5)
>>> fahrenheit_entry.insert(0, "32.0")
>>> celsius_label = tk.Label(root, text="Celsius:")
>>> celsius_label.grid(row=0, column=1, padx=5, pady=5)
>>> celsius_entry = tk.Entry(root)
>>> celsius_entry.grid(row=1, column=1, padx=5, pady=5)
>>> celsius_entry.insert(0, "0.0")
>>> f_to_c_button = tk.Button(root, text=">>>>", command=fahrenheit_to_celsius)
>>> f_to_c_button.grid(row=2, column=0, padx=5, pady=5)
>>> c_to_f_button = tk.Button(root, text="<<<<", command=celsius_to_fahrenheit)
>>> c_to_f_button.grid(row=2, column=1, padx=5, pady=5)
>>> root.mainloop()
