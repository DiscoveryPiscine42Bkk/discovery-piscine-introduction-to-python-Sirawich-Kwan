#!/usr/bin/env python3

input_number = input("Give me a number: ")
try:
    input_number = float(input_number)
except:
    print("input isn't a number")
    exit()
if int(input_number) == float(input_number):
    print("This number is an integer.")
else:
    print("This number is a decimal.")