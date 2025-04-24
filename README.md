-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CPU Viewer

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Project Structure](#project-structure)
5. [Notes](#notes)
6. [License](#license)

## Introduction
The **CPU Viewer** tool provides a real-time visualization of **CPU and Memory usage**. It is useful for developers, system administrators, and tech enthusiasts who need a quick way to monitor system performance through clear and dynamic graphical charts.

## Installation

### Setting up the Virtual Environment
Create a virtual environment inside the `CPU Viewer` directory:

```bash
python -m venv "CPU Viewer/venv"
```

Activate the virtual environment:

On **Windows**:
```bash
CPU Viewer\venv\Scripts.\activate
```

On **macOS/Linux**:
```bash
source "CPU Viewer/venv/bin/activate"
```

### Install the necessary packages

```bash
pip install psutil matplotlib
```

### Creating an Executable

Install PyInstaller:

```bash
pip install pyinstaller
```

Generate the executable:

```bash
pyinstaller --onefile --name CPUVw.py
```

Find the executable:  
The executable file will be located in the `dist` folder as `CPUVw.exe`.

## Usage

### Run the script:

To run the script directly:
```bash
python script.py
```

Or, click the executable file located in the `dist` folder.

The program will display real-time graphs showing both **CPU and Memory usage**.

If you prefer to use the program without setting up the environment or building the executable, simply run the pre-built `CPUVw.exe` directly.

## Project Structure

```
CPU Viewer/
├── venv            # Virtual environment       
├── CPUVw.exe       # Executable file
├── CPUVw.py        # Main script file
├── LICENSE.txt     # License file
└── README.md       # Documentation file
```

## Notes

- Ensure Python is installed on your system if running the script directly.
- Always activate the virtual environment before running the script to ensure all dependencies are properly managed.

markx98!
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
