import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
import subprocess
import os

class ConverterLauncherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("⚙️ Smart Converter Launcher")
        self.root.geometry("420x450")
        self.root.resizable(False, False)

        # Set style theme
        self.root.style.theme_use("morph")  # modern look

        # Scrollable canvas
        canvas = tk.Canvas(root, borderwidth=0, background="#f8f9fa", highlightthickness=0)
        frame = ttk.Frame(canvas, padding=10)
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(-1 * (e.delta // 120), "units"))

        # Title
        ttk.Label(frame, text="🔥 Converter Launcher", font="Calibri 24 bold").pack(pady=(0, 15))

        # Converter buttons
        self.create_converter_button(frame, "Area Converter", "AreaConverter")
        self.create_converter_button(frame, "Length Converter", "LenConverter")
        self.create_converter_button(frame, "Speed Converter", "SpeedConverter")
        self.create_converter_button(frame, "Pressure Converter", "PressureConverter")
        self.create_converter_button(frame, "Power Converter", "PowerConverter")
        self.create_converter_button(frame, "Weight Converter", "WeightConverter")
        self.create_converter_button(frame, "Volume Converter", "VolumeConverter")
        self.create_converter_button(frame, "Temperature Converter", "TemperatureConverter")
        self.create_converter_button(frame, "Energy Converter", "EnergyConverter")
        self.create_converter_button(frame, "Force Converter", "ForceConverter")
        self.create_converter_button(frame, "Digital Storage Converter", "DigitalStorageConverter")
        self.create_converter_button(frame, "Current Converter", "CurrentConverter")

        # Theme dropdown
        ttk.Label(frame, text="🎨 Theme", font="Calibri 12 bold").pack(pady=(10, 2))
        self.theme_var = tk.StringVar(value="morph")
        theme_dropdown = ttk.Combobox(frame, textvariable=self.theme_var, values=root.style.theme_names(), state="readonly", width=20)
        theme_dropdown.pack(pady=5)
        theme_dropdown.bind("<<ComboboxSelected>>", self.change_theme)

    def create_converter_button(self, parent, label, file_tag):
        ttk.Button(parent, text=label, width=30, bootstyle="primary-outline", command=lambda: self.launch_converter(file_tag)).pack(pady=6)

    def get_converter_path(self, converter_name):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_dir, "converters", f"GUI_{converter_name}.py")

    def launch_converter(self, converter_name):
        converter_path = self.get_converter_path(converter_name)
        if os.path.exists(converter_path):
            subprocess.run(["python", converter_path])
        else:
            print(f"⚠️ Error: {converter_name} not found!")

    def change_theme(self, event):
        selected_theme = self.theme_var.get()
        self.root.style.theme_use(selected_theme)

def run_converter_launcher():
    root = ttk.Window(themename="morph")
    app = ConverterLauncherApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_converter_launcher()
