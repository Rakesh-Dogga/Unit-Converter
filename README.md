# Unit Converter

A simple, terminal-based unit converter built using Python. This project allows users to convert values between different units of measurement through an interactive command-line interface.

## Features

- **Length Conversion:** Convert between kilometers, meters, centimeters, and millimeters.
- **Temperature Conversion:** Convert between Celsius, Fahrenheit, and Kelvin.
- **Speed Conversion:** Convert between meters per second, kilometers per hour, miles per hour, and knots.
- **Time Conversion:** Convert between seconds, minutes, hours, days, and weeks.
- **Volume Conversion:** Convert between liters, milliliters, cubic meters, and US gallons.
- **Digital Storage:** Convert between bytes, kb, mb, gb, tb, pb and eb.
- **Unit Selection:** Displays the supported units for the selected converter.
- **Input Validation:** Checks whether the selected converter and units are supported.

## Technologies Used

- Python
- Dictionaries and functions
- Conditional statements
- Exception handling
- Git and GitHub

## Project Structure

```text
python-unit-converter/
├── main.py
├── .gitignore
└── README.md
```

## How to Run

1. Install Python on your computer.
2. Clone this repository:

   ```bash
   git clone https://github.com/Rakesh-Dogga/Unit-Converter.git
   ```

3. Navigate to the project directory:

   ```bash
   cd Unit-Converter
   ```

4. Run the program:

   ```bash
   python main.py
   ```

## Example Usage

```
==========
Unit Converter
==========

Available converters: 
Length
Temperature
Speed
Time
Volume
Digital Storage
Enter selected converter: digital storage

Available digital storage units: 
 bit    - Bit
 byte   - Byte
 kb     - Kilobyte
 mb     - Megabyte
 gb     - Gigabyte
 tb     - Terabyte
 pb     - Petabyte
 eb     - Exabyte

Convert from units: tb
Enter value: 10000
Convert to units: kb

==============================
CONVERSION RESULT
Result: 1e+13 kb
==============================
```

## Learning Objectives

This project is intended to practice Python fundamentals, including:

- Defining and calling functions
- Using dictionaries to store conversion factors
- Handling user input
- Validating input values and units
- Using exceptions for error handling
- Organizing code into reusable functions

