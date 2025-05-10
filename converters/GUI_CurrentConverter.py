import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk

class CurrentConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('650x400')
        self.root.resizable(False, False)
        self.root.title('Electric Current Converter')

        # Conversion Factors
        self.conversion_factors = {
            "Amperes": 1,
            "Milliamperes": 1000,
            "Kiloamperes": 0.001
        }

        # Title Label
        title_label = Label(self.root, text='Electric Current Converter', font='Calibri 24 bold', pady=10)
        title_label.pack()

        # Input Section
        input_label = ttk.Label(self.root, text="Enter Current Value:", font='Calibri 12')
        input_label.pack(pady=2)

        self.entry_var = tk.StringVar()
        entry = ttk.Entry(self.root, textvariable=self.entry_var, width=15, font='Calibri 14')
        entry.pack(pady=5)

        # Dropdown Frame
        dropdown_frame = ttk.Frame(self.root)

        # From Dropdown
        from_label = ttk.Label(dropdown_frame, text="From:", font='Calibri 12')
        from_label.pack(side='left', padx=5)
        self.from_var = tk.StringVar(value="Amperes")
        from_dropdown = ttk.Combobox(dropdown_frame, textvariable=self.from_var, values=list(self.conversion_factors.keys()), state="readonly", width=15)
        from_dropdown.pack(side='left', padx=5)

        # To Dropdown
        to_label = ttk.Label(dropdown_frame, text="To:", font='Calibri 12')
        to_label.pack(side='left', padx=5)
        self.to_var = tk.StringVar(value="Milliamperes")
        to_dropdown = ttk.Combobox(dropdown_frame, textvariable=self.to_var, values=list(self.conversion_factors.keys()), state="readonly", width=15)
        to_dropdown.pack(side='left', padx=5)

        dropdown_frame.pack(pady=5)

        # Convert Button
        button = ttk.Button(self.root, text='Convert', command=self.convert_current)
        button.pack(pady=10)

        # Output Field
        self.output_string = tk.StringVar()
        self.output_label = ttk.Label(self.root, textvariable=self.output_string, font='calibri 18', foreground='blue')
        self.output_label.pack(pady=10)

        # Theme Selection
        theme_label = ttk.Label(self.root, text="Select Theme:", font='Calibri 12')
        theme_label.pack(pady=5)

        self.theme_var = tk.StringVar(value="cosmo")
        theme_dropdown = ttk.Combobox(self.root, textvariable=self.theme_var, values=self.root.style.theme_names(), state="readonly", width=15)
        theme_dropdown.pack(pady=5)
        theme_dropdown.bind("<<ComboboxSelected>>", self.change_theme)

    def convert_current(self):
        try:
            value = float(self.entry_var.get())
            from_unit = self.from_var.get()
            to_unit = self.to_var.get()

            if from_unit in self.conversion_factors and to_unit in self.conversion_factors:
                value_in_amperes = value / self.conversion_factors[from_unit]
                converted_value = value_in_amperes * self.conversion_factors[to_unit]

                self.output_string.set(f"{value:.2f} {from_unit} = {converted_value:.4f} {to_unit}")
            else:
                self.output_string.set("Error: Invalid unit selection")
        except ValueError:
            self.output_string.set("Error: Enter a valid number")

    def change_theme(self, event):
        selected_theme = self.theme_var.get()
        self.root.style.theme_use(selected_theme)

def run_current_converter():
    root = ttk.Window(themename='cosmo')
    app = CurrentConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_current_converter()
