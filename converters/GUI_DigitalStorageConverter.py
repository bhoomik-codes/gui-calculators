import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk

class StorageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Storage Converter")
        self.root.geometry("600x400")

        self.conversion_factors = {
            "Byte (B)": 1,
            "Kilobyte (KB)": 1024,
            "Megabyte (MB)": 1024**2,
            "Gigabyte (GB)": 1024**3,
            "Terabyte (TB)": 1024**4,
            "Petabyte (PB)": 1024**5
        }

        Label(root, text="Digital Storage Converter", font='Calibri 24 bold').pack(pady=10)

        ttk.Label(root, text="Enter Storage Value:", font='Calibri 12').pack()
        self.entry_var = tk.StringVar()
        ttk.Entry(root, textvariable=self.entry_var, width=15, font='Calibri 14').pack(pady=5)

        dropdown_frame = ttk.Frame(root)
        dropdown_frame.pack(pady=5)

        ttk.Label(dropdown_frame, text="From:", font='Calibri 12').pack(side='left', padx=5)
        self.from_var = tk.StringVar(value="Byte (B)")
        from_dropdown = ttk.Combobox(dropdown_frame, textvariable=self.from_var, values=list(self.conversion_factors.keys()), state="readonly", width=20)
        from_dropdown.pack(side='left', padx=5)

        ttk.Label(dropdown_frame, text="To:", font='Calibri 12').pack(side='left', padx=5)
        self.to_var = tk.StringVar(value="Megabyte (MB)")
        to_dropdown = ttk.Combobox(dropdown_frame, textvariable=self.to_var, values=list(self.conversion_factors.keys()), state="readonly", width=20)
        to_dropdown.pack(side='left', padx=5)

        ttk.Button(root, text="Convert", command=self.convert_storage).pack(pady=10)

        self.output_string = tk.StringVar()
        ttk.Label(root, textvariable=self.output_string, font='Calibri 16', foreground='green').pack()

        ttk.Label(root, text="Select Theme:", font='Calibri 12').pack(pady=5)
        self.theme_var = tk.StringVar(value="cosmo")
        theme_dropdown = ttk.Combobox(root, textvariable=self.theme_var, values=root.style.theme_names(), state="readonly", width=15)
        theme_dropdown.pack(pady=5)
        theme_dropdown.bind("<<ComboboxSelected>>", self.change_theme)

    def convert_storage(self):
        try:
            value = float(self.entry_var.get())
            from_unit = self.from_var.get()
            to_unit = self.to_var.get()

            value_in_bytes = value * self.conversion_factors[from_unit]
            converted_value = value_in_bytes / self.conversion_factors[to_unit]

            self.output_string.set(f"{value:.2f} {from_unit} = {converted_value:.4f} {to_unit}")
        except ValueError:
            self.output_string.set("Please enter a valid number.")

    def change_theme(self, event):
        selected_theme = self.theme_var.get()
        self.root.style.theme_use(selected_theme)

def run_storage_converter():
    root = ttk.Window(themename="cosmo")
    app = StorageConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_storage_converter()
