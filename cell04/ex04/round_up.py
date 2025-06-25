#!/usr/bin/env python3

enter_number = input("Enter a number: ")
try:
    num1 = int(float(enter_number))
    num2 = float(enter_number)
except:
    print("Input isn't a number")
    exit()

if num1 == num2:
    print(num1)
elif num2 < 0:
    print(num1)
else:
    print(num1 + 1)