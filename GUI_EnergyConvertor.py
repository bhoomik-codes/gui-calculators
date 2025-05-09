import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk

class EnergyConvertorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Energy Convertor")
        self.root.resizable(False, False)
        self.frame = tk.Frame(self.root)
        # self.frame.pack(fill=tk.BOTH, expand=True)

        self.conversion_factors = {
        1: 'joules',
        2: 'kilojoules',
        3: 'calories',
        4: 'kilocalories',
        5: 'watt-hours',
        6: 'kilowatt-hours'
        }

        # Title Label
        title_label = Label(self.root, text='Energy Converter', font='Calibri 24 bold', pady=10)
        title_label.pack()

        # Input Section
        input_label = ttk.Label(self.root, text="Enter Energy Value:", font='Calibri 12')
        input_label.pack(pady=2)

        self.entry_var = tk.StringVar()
        entry = ttk.Entry(self.root, textvariable=self.entry_var, width=15, font='Calibri 14')
        entry.pack(pady=5)

        # Dropdown Frame
        dropdown_frame = ttk.Frame(self.root)

        # From Dropdown
        from_label = ttk.Label(dropdown_frame, text="From:", font='Calibri 12')
        from_label.pack(side='left', padx=5)
        self.from_var = tk.StringVar(value="")
        from_dropdown = ttk.Combobox(dropdown_frame, textvariable=self.from_var, values=list(self.conversion_factors.keys()), state="readonly", width=15)
        from_dropdown.pack(side='left', padx=5)