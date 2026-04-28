# Project Description

**Basic Calculator** is a simple Python command-line application that takes two numbers as input from the user and performs basic arithmetic operations with error handling.

## Features

- Addition
- Subtraction
- Multiplication
- Input validation in `main.py` (catches non-integer input)
- Operation-level error handling in `utils.py` (catches type errors)

## Project Structure

- `src/main.py` — Entry point, takes user input with validation and displays results
- `src/utils.py` — Contains arithmetic functions (`add`, `subtract`, `multiply`) with a shared error handler
