import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk

class TemperatureConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("500x400")

        self.units = ["Celsius", "Fahrenheit", "Kelvin"]

        title = Label(self.root, text="🌡️ Temperature Converter", font="Calibri 24 bold", pady=10)
        title.pack()

        input_label = ttk.Label(self.root, text="Enter Temperature Value:", font="Calibri 12")
        input_label.pack(pady=5)

        self.value_var = tk.StringVar()
        entry = ttk.Entry(self.root, textvariable=self.value_var, font="Calibri 14", width=20)
        entry.pack(pady=5)

        # Dropdowns
        dropdown_frame = ttk.Frame(self.root)
        dropdown_frame.pack(pady=5)

        from_label = ttk.Label(dropdown_frame, text="From:", font="Calibri 12")
        from_label.pack(side="left", padx=5)
        self.from_var = tk.StringVar(value="Celsius")
        from_dropdown = ttk.Combobox(dropdown_frame, textvariable=self.from_var, values=self.units, state="readonly", width=15)
        from_dropdown.pack(side="left", padx=5)

        to_label = ttk.Label(dropdown_frame, text="To:", font="Calibri 12")
        to_label.pack(side="left", padx=5)
        self.to_var = tk.StringVar(value="Fahrenheit")
        to_dropdown = ttk.Combobox(dropdown_frame, textvariable=self.to_var, values=self.units, state="readonly", width=15)
        to_dropdown.pack(side="left", padx=5)

        convert_btn = ttk.Button(self.root, text="Convert", command=self.convert_temperature)
        convert_btn.pack(pady=10)

        self.result_var = tk.StringVar()
        result_label = ttk.Label(self.root, textvariable=self.result_var, font="Calibri 16", foreground="blue")
        result_label.pack(pady=10)

        # Theme switcher
        theme_label = ttk.Label(self.root, text="Select Theme:", font="Calibri 12")
        theme_label.pack(pady=5)
        self.theme_var = tk.StringVar(value="cosmo")
        theme_dropdown = ttk.Combobox(self.root, textvariable=self.theme_var, values=self.root.style.theme_names(), state="readonly", width=15)
        theme_dropdown.pack(pady=5)
        theme_dropdown.bind("<<ComboboxSelected>>", self.change_theme)

    def convert_temperature(self):
        try:
            value = float(self.value_var.get())
            from_unit = self.from_var.get()
            to_unit = self.to_var.get()

            result = self.perform_conversion(value, from_unit, to_unit)
            if result is not None:
                self.result_var.set(f"{value:.2f} {from_unit} = {result:.2f} {to_unit}")
            else:
                self.result_var.set("Error: Conversion not possible")
        except ValueError:
            self.result_var.set("Error: Enter a valid number")

    def perform_conversion(self, val, from_unit, to_unit):
        if from_unit == to_unit:
            return val
        if from_unit == "Celsius":
            return self.celsius_to(val, to_unit)
        elif from_unit == "Fahrenheit":
            return self.fahrenheit_to(val, to_unit)
        elif from_unit == "Kelvin":
            return self.kelvin_to(val, to_unit)
        return None

    def celsius_to(self, val, to_unit):
        if to_unit == "Fahrenheit":
            return (val * 9/5) + 32
        elif to_unit == "Kelvin":
            return val + 273.15
        return None

    def fahrenheit_to(self, val, to_unit):
        if to_unit == "Celsius":
            return (val - 32) * 5/9
        elif to_unit == "Kelvin":
            return (val - 32) * 5/9 + 273.15
        return None

    def kelvin_to(self, val, to_unit):
        if to_unit == "Celsius":
            return val - 273.15
        elif to_unit == "Fahrenheit":
            return (val - 273.15) * 9/5 + 32
        return None

    def change_theme(self, event):
        selected_theme = self.theme_var.get()
        self.root.style.theme_use(selected_theme)

def run_app():
    root = ttk.Window(themename="cosmo")
    app = TemperatureConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()
