>>> import tkinter as tk
>>> from tkinter import ttk
>>> TAX_RATE = 0.15
>>> STANDARD_DEDUCTION = 8000.0
>>> DEPENDENT_DEDUCTION = 2000.0
>>> class TaxCalculatorGUI:
...     def __init__(self, master):
...         self.master = master
...         master.title("Tax Calculator")
...         self.income_label = ttk.Label(master, text="Enter your income:")
...         self.income_label.grid(row=0, column=0, sticky="e")
...         self.income_entry = ttk.Entry(master)
...         self.income_entry.grid(row=0, column=1, sticky="ew")
...         self.dependent_label = ttk.Label(master, text="Number of dependents:")
...         self.dependent_label.grid(row=1, column=0, sticky="e")
...         self.dependent_entry = ttk.Entry(master)
...         self.dependent_entry.grid(row=1, column=1, sticky="ew")
...         self.calculate_button = ttk.Button(master, text="Calculate Tax", command=self.calculate_tax)
...         self.calculate_button.grid(row=2, column=0, columnspan=2, pady=10)
...         self.tax_result_label = ttk.Label(master, text="")
...         self.tax_result_label.grid(row=3, column=0, columnspan=2)
...
>>> def calculate_tax(self):
...     try:
...         income = float(self.income_entry.get())
...         dependents = int(self.dependent_entry.get())
...         deductions = STANDARD_DEDUCTION + (DEPENDENT_DEDUCTION * dependents)
...         taxable_income = income - deductions
...         tax = taxable_income * TAX_RATE
...         self.tax_result_label.config(text=f"Your tax amount is: ${tax:.2f}")except ValueError:
...             self.tax_result_label.config(text="Invalid input. Please enter numbers.")
...
  File "<python-input-6>", line 8
    self.tax_result_label.config(text=f"Your tax amount is: ${tax:.2f}")except ValueError:
                                                                        ^^^^^^
SyntaxError: invalid syntax
>>> root = tk.Tk()
>>> gui = TaxCalculatorGUI(root)
Traceback (most recent call last):
  File "<python-input-8>", line 1, in <module>
    gui = TaxCalculatorGUI(root)
  File "<python-input-5>", line 13, in __init__
    self.calculate_button = ttk.Button(master, text="Calculate Tax", command=self.calculate_tax)
                                                                             ^^^^^^^^^^^^^^^^^^
AttributeError: 'TaxCalculatorGUI' object has no attribute 'calculate_tax'
>>> root.mainloop()
