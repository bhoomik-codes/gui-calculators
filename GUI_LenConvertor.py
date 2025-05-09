import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk

# Length conversion factors (relative to meters)
conversion_factors = {
    "Meters": 1,
    "Kilometers": 0.001,
    "Centimeters": 100,
    "Millimeters": 1000,
    "Inches": 39.3701,
    "Feet": 3.28084,
    "Yards": 1.09361,
    "Miles": 0.000621371
}

class LengthConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('650x500')
        self.root.resizable(False, False)
        self.root.title('Length Converter')

        # Title Label
        title_label = Label(self.root, text='Length Converter', font='Calibri 24 bold', pady=10)
        title_label.pack()

        # Input Section
        input_label = ttk.Label(self.root, text="Enter Value:", font='Calibri 12')
        input_label.pack(pady=2)

        self.entry_var = tk.StringVar()
        entry = ttk.Entry(self.root, textvariable=self.entry_var, width=15, font='Calibri 14')
        entry.pack(pady=5)

        # From Unit Selection
        from_label = ttk.Label(self.root, text="Convert From:", font='Calibri 12')
        from_label.pack(pady=2)

        self.from_var = tk.StringVar(value="Meters")
        from_dropdown = ttk.Combobox(self.root, textvariable=self.from_var, values=list(conversion_factors.keys()), state="readonly", width=15)
        from_dropdown.pack(pady=5)

        # To Unit Selection
        to_label = ttk.Label(self.root, text="Convert To:", font='Calibri 12')
        to_label.pack(pady=2)

        self.to_var = tk.StringVar(value="Kilometers")
        to_dropdown = ttk.Combobox(self.root, textvariable=self.to_var, values=list(conversion_factors.keys()), state="readonly", width=15)
        to_dropdown.pack(pady=5)

        # Convert Button
        button = ttk.Button(self.root, text='Convert', command=self.convert_length)
        button.pack(pady=10)

        # Output Field
        self.output_string = tk.StringVar()
        output_label = ttk.Label(self.root, textvariable=self.output_string, font='calibri 18', foreground='blue')
        output_label.pack(pady=10)

        # Theme Selection Section
        theme_label = ttk.Label(self.root, text="Select Theme:", font='Calibri 12')
        theme_label.pack(pady=5)

        self.theme_var = tk.StringVar(value="cosmo")
        theme_dropdown = ttk.Combobox(self.root, textvariable=self.theme_var, values=self.root.style.theme_names(), state="readonly", width=15)
        theme_dropdown.pack(pady=5)
        theme_dropdown.bind("<<ComboboxSelected>>", self.change_theme)

    def convert_length(self):
        try:
            value = float(self.entry_var.get())
            from_unit = self.from_var.get()
            to_unit = self.to_var.get()

            if from_unit in conversion_factors and to_unit in conversion_factors:
                value_in_meters = value / conversion_factors[from_unit]
                converted_value = value_in_meters * conversion_factors[to_unit]
                self.output_string.set(f"{value:.2f} {from_unit} = {converted_value:.4f} {to_unit}")
            else:
                self.output_string.set("Error: Invalid unit selection")
        except ValueError:
            self.output_string.set("Error: Enter a valid number")

    def change_theme(self, event):
        selected_theme = self.theme_var.get()
        self.root.style.theme_use(selected_theme)

def run_converter():
    root = ttk.Window(themename='cosmo')
    app = LengthConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_converter()
