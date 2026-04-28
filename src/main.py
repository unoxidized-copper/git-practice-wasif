import datetime
from utils import add, subtract, multiply

print("My name is wasif")
print(f"Today's date is {datetime.date.today()}")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"Addition: {add(a, b)}")
print(f"Subtraction: {subtract(a, b)}")
print(f"Multiplication: {multiply(a, b)}")
