import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk

class WeightConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weight Converter")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        # Title
        Label(self.root, text="Weight Converter", font="Calibri 20 bold", pady=10).pack()

        # Input
        ttk.Label(self.root, text="Enter Weight:", font="Calibri 12").pack(pady=2)
        self.entry_var = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.entry_var, width=20, font="Calibri 14").pack(pady=5)

        # Units
        units = ["Grams", "Kilograms", "Pounds", "Ounces", "Tonnes"]

        dropdown_frame = ttk.Frame(self.root)
        ttk.Label(dropdown_frame, text="From:", font="Calibri 12").pack(side='left', padx=5)
        self.from_unit = tk.StringVar(value="Grams")
        ttk.Combobox(dropdown_frame, textvariable=self.from_unit, values=units, state="readonly", width=12).pack(side='left', padx=5)
        ttk.Label(dropdown_frame, text="To:", font="Calibri 12").pack(side='left', padx=5)
        self.to_unit = tk.StringVar(value="Kilograms")
        ttk.Combobox(dropdown_frame, textvariable=self.to_unit, values=units, state="readonly", width=12).pack(side='left', padx=5)
        dropdown_frame.pack(pady=10)

        # Button and Output
        ttk.Button(self.root, text="Convert", command=self.convert_weight).pack(pady=10)
        self.output_var = tk.StringVar()
        ttk.Label(self.root, textvariable=self.output_var, font="Calibri 16", foreground="blue").pack(pady=10)

        # Theme
        ttk.Label(self.root, text="Select Theme:", font='Calibri 12').pack(pady=5)
        self.theme_var = tk.StringVar(value="minty")
        theme_dropdown = ttk.Combobox(self.root, textvariable=self.theme_var, values=self.root.style.theme_names(), state="readonly", width=15)
        theme_dropdown.pack(pady=5)
        theme_dropdown.bind("<<ComboboxSelected>>", self.change_theme)

        # Conversion factors (to grams)
        self.to_grams = {
            "Grams": 1,
            "Kilograms": 1000,
            "Pounds": 453.592,
            "Ounces": 28.3495,
            "Tonnes": 1e6
        }

    def convert_weight(self):
        try:
            value = float(self.entry_var.get())
            grams = value * self.to_grams[self.from_unit.get()]
            result = grams / self.to_grams[self.to_unit.get()]
            self.output_var.set(f"{value:.2f} {self.from_unit.get()} = {result:.4f} {self.to_unit.get()}")
        except ValueError:
            self.output_var.set("Please enter a valid number")

    def change_theme(self, event):
        self.root.style.theme_use(self.theme_var.get())

def run_weight_converter():
    root = ttk.Window(themename="minty")
    app = WeightConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_weight_converter()
