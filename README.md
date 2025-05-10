# GUI-Calculators
Some simple GUI based calculators I made, Planning to  upload a MultiCalculator with all the calculators interlinked
# 🧼 GUI\_Calcs - Multi-Purpose Unit Converter Toolkit

A modern, beginner-friendly collection of **Tkinter + ttkbootstrap** based unit converters. Each calculator has a clean themed GUI, dropdown-based unit selection, and supports real-time conversion using internally defined conversion factors.

> 🎯 Built to be modular, stylish, and easily extendable.

---

## 📁 Project Structure

```
GUI_Calcs/
│
├── converters/                # All individual converter scripts
│   ├── GUI_AreaConverter.py
│   ├── GUI_CurrentConverter.py
│   ├── GUI_DigitalStorageConverter.py
│   ├── GUI_EnergyConverter.py
│   ├── GUI_ForceConverter.py
│   ├── GUI_LenConverter.py
│   ├── GUI_PowerConverter.py
│   ├── GUI_PressureConverter.py
│   ├── GUI_SpeedConverter.py
│   ├── GUI_TemperatureConverter.py
│   ├── GUI_VolumeConverter.py
│   └── GUI_WeightConverter.py
│
└── launcher.py               # Main app launcher with theme selection and scrollable GUI
```

---

## 🧹 Features

* 🌀 **Scrollable Launcher GUI** – View all converters even on small screens
* 🎨 **Modern Themes** – Powered by `ttkbootstrap` (e.g., Cosmo, Darkly, Morph)
* 🧠 **Conversion Logic** – Each converter uses internal conversion factor dictionaries
* ⚡ **Fast and Lightweight** – No external dependencies beyond `ttkbootstrap`
* 🔌 **Modular Design** – Add your own converters easily inside the `/converters` folder

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x
* `ttkbootstrap`
  Install with:

  ```bash
  pip install ttkbootstrap
  ```

---

### Run the App

Run the launcher from a terminal or IDE:

```bash
python launcher.py
```

> ⚠️ Double-clicking the file may cause **"cannot open converter"** errors due to path issues. Always launch via terminal or IDE, or ensure you’ve applied the relative path fix in `launcher.py`.

---

## 🛠️ Add a New Converter

1. Create a new file in `converters/` like: `GUI_MyCustomConverter.py`
2. Use the same class-based structure as existing files
3. Name your class something like `MyCustomConverterApp`
4. Add the file name to the launcher’s converter list

---

## 💼 Converters Included

* ✅ Area Converter
* ✅ Current Converter
* ✅ Digital Storage Converter
* ✅ Energy Converter
* ✅ Force Converter
* ✅ Length Converter
* ✅ Power Converter
* ✅ Pressure Converter
* ✅ Speed Converter
* ✅ Temperature Converter
* ✅ Volume Converter
* ✅ Weight Converter

---

## 💡 Future Ideas

* Add light/dark theme toggle
* Support for custom units via config file
* History of conversions
* Packaging as an executable with PyInstaller

---

## 🧑‍💻 Author

Made with 💻 and 🧠 by **Bhoomik Sevta**

---
