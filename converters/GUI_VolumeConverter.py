import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk

class VolumeConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Volume Converter")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        Label(self.root, text="Volume Converter", font="Calibri 20 bold", pady=10).pack()

        ttk.Label(self.root, text="Enter Volume:", font="Calibri 12").pack(pady=2)
        self.entry_var = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.entry_var, width=20, font="Calibri 14").pack(pady=5)

        units = ["Milliliters", "Liters", "Cubic Meters", "Cubic Inches", "Cubic Feet", "Gallons"]

        dropdown_frame = ttk.Frame(self.root)
        ttk.Label(dropdown_frame, text="From:", font="Calibri 12").pack(side='left', padx=5)
        self.from_unit = tk.StringVar(value="Liters")
        ttk.Combobox(dropdown_frame, textvariable=self.from_unit, values=units, state="readonly", width=15).pack(side='left', padx=5)
        ttk.Label(dropdown_frame, text="To:", font="Calibri 12").pack(side='left', padx=5)
        self.to_unit = tk.StringVar(value="Milliliters")
        ttk.Combobox(dropdown_frame, textvariable=self.to_unit, values=units, state="readonly", width=15).pack(side='left', padx=5)
        dropdown_frame.pack(pady=10)

        ttk.Button(self.root, text="Convert", command=self.convert_volume).pack(pady=10)
        self.output_var = tk.StringVar()
        ttk.Label(self.root, textvariable=self.output_var, font="Calibri 16", foreground="blue").pack(pady=10)

        ttk.Label(self.root, text="Select Theme:", font='Calibri 12').pack(pady=5)
        self.theme_var = tk.StringVar(value="journal")
        theme_dropdown = ttk.Combobox(self.root, textvariable=self.theme_var, values=self.root.style.theme_names(), state="readonly", width=15)
        theme_dropdown.pack(pady=5)
        theme_dropdown.bind("<<ComboboxSelected>>", self.change_theme)

        self.to_ml = {
            "Milliliters": 1,
            "Liters": 1000,
            "Cubic Meters": 1e6,
            "Cubic Inches": 16.3871,
            "Cubic Feet": 28316.8,
            "Gallons": 3785.41
        }

    def convert_volume(self):
        try:
            value = float(self.entry_var.get())
            ml = value * self.to_ml[self.from_unit.get()]
            result = ml / self.to_ml[self.to_unit.get()]
            self.output_var.set(f"{value:.2f} {self.from_unit.get()} = {result:.4f} {self.to_unit.get()}")
        except ValueError:
            self.output_var.set("Please enter a valid number")

    def change_theme(self, event):
        self.root.style.theme_use(self.theme_var.get())

def run_volume_converter():
    root = ttk.Window(themename="journal")
    app = VolumeConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_volume_converter()
