# Interactive Calculator & Unit Converter

A beginner-friendly command-line program written in Python that combines an arithmetic calculator, a unit converter, and a currency converter in one interactive menu. Built as a practice project to master core Python fundamentals: syntax, conditionals, functions, loops, and user input.

## Features

- **Arithmetic Calculator** — Addition, subtraction, multiplication, and division with divide-by-zero protection.
- **Unit Converter**
  - Kilometers <-> Miles
  - Miles <-> Kilometers
  - Celsius <-> Fahrenheit
- **Currency Converter** — Convert between USD, EUR, GBP, and INR using built-in fixed sample rates.
- **Input Validation** — Every prompt uses a `while` loop, so invalid numbers or menu choices never crash the program.

## Getting Started

### Prerequisites

- Python 3 installed on your machine (no external libraries required).

### Running the Program

1. Clone the repository:

   ```bash
   git clone https://github.com/Divyanshu11007/Interactive-Calculator---Unit-Converter.git
   cd Interactive-Calculator---Unit-Converter
   ```

2. Run the program:

   ```bash
   python calculator.py
   ```

## How It Works

The program opens with a main menu:

```
========================================
 Interactive Calculator & Unit Converter
========================================

MAIN MENU
1. Arithmetic calculator
2. Unit converter
3. Currency converter
4. Exit
Choose an option (1-4):
```

Pick an option from `1` to `4`. After each calculation, choose whether to return to the main menu (`y`) or quit (`n`). Invalid inputs — letters where numbers are expected, or unsupported menu choices — simply re-prompt instead of crashing.

## Example Session

```
--- Arithmetic Calculator ---
Choose an operation (+, -, *, /): *
Enter the first number: 5
Enter the second number: 3

5 * 3 = 15
```

## Notes

- Currency rates are **fixed sample values** for learning purposes, not live exchange rates.
- Distance and temperature conversion results are rounded for clean output.

## Project Goal

This project demonstrates:

- Fundamental Python syntax and operators
- Conditional statements (`if` / `elif` / `else`)
- Functions with parameters and return values
- `while` loops for input validation
- Handling user input with `input()` and `float()`
- Basic error handling with `try` / `except`

## License

This project is free to use and modify for learning purposes.
