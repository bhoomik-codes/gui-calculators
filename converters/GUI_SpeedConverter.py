import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk

class SpeedConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Converter")
        self.root.geometry("600x400")

        # Conversion factors to meters per second (m/s)
        self.conversion_factors = {
            "Meters/second": 1,
            "Kilometers/hour": 1 / 3.6,
            "Miles/hour": 0.44704,
            "Feet/second": 0.3048,
            "Knots": 0.514444
        }

        Label(root, text="Speed Converter", font='Calibri 24 bold').pack(pady=10)

        ttk.Label(root, text="Enter Speed Value:", font='Calibri 12').pack()
        self.entry_var = tk.StringVar()
        ttk.Entry(root, textvariable=self.entry_var, width=15, font='Calibri 14').pack(pady=5)

        dropdown_frame = ttk.Frame(root)
        dropdown_frame.pack(pady=5)

        ttk.Label(dropdown_frame, text="From:", font='Calibri 12').pack(side='left', padx=5)
        self.from_var = tk.StringVar(value="Kilometers/hour")
        from_dropdown = ttk.Combobox(dropdown_frame, textvariable=self.from_var, values=list(self.conversion_factors.keys()), state="readonly", width=20)
        from_dropdown.pack(side='left', padx=5)

        ttk.Label(dropdown_frame, text="To:", font='Calibri 12').pack(side='left', padx=5)
        self.to_var = tk.StringVar(value="Miles/hour")
        to_dropdown = ttk.Combobox(dropdown_frame, textvariable=self.to_var, values=list(self.conversion_factors.keys()), state="readonly", width=20)
        to_dropdown.pack(side='left', padx=5)

        ttk.Button(root, text="Convert", command=self.convert_speed).pack(pady=10)

        self.output_string = tk.StringVar()
        ttk.Label(root, textvariable=self.output_string, font='Calibri 16', foreground='green').pack()

        # Theme selector
        ttk.Label(root, text="Select Theme:", font='Calibri 12').pack(pady=5)
        self.theme_var = tk.StringVar(value="cosmo")
        theme_dropdown = ttk.Combobox(root, textvariable=self.theme_var, values=root.style.theme_names(), state="readonly", width=15)
        theme_dropdown.pack(pady=5)
        theme_dropdown.bind("<<ComboboxSelected>>", self.change_theme)

    def convert_speed(self):
        try:
            value = float(self.entry_var.get())
            from_unit = self.from_var.get()
            to_unit = self.to_var.get()

            value_in_mps = value * self.conversion_factors[from_unit]
            converted_value = value_in_mps / self.conversion_factors[to_unit]

            self.output_string.set(f"{value:.2f} {from_unit} = {converted_value:.4f} {to_unit}")
        except ValueError:
            self.output_string.set("Please enter a valid number.")

    def change_theme(self, event):
        selected_theme = self.theme_var.get()
        self.root.style.theme_use(selected_theme)

def run_speed_converter():
    root = ttk.Window(themename="cosmo")
    app = SpeedConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_speed_converter()
