import datetime
from utils import add, subtract, multiply

print("My name is wasif")
print(f"Today's date is {datetime.date.today()}")

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
except ValueError:
    print("Error: Invalid input. Please enter valid integers.")
    exit(1)

print(f"Addition: {add(a, b)}")
print(f"Subtraction: {subtract(a, b)}")
print(f"Multiplication: {multiply(a, b)}")
