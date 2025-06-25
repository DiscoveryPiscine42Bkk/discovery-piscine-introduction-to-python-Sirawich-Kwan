#!/usr/bin/env python3

first_number = input("Give me the first number: ")
second_number = input("Give me the second number: ")
print("Thank you!")
try:
    first_number = int(first_number)
    second_number = int(second_number)
except:
    print("Please put number as input or only one number")
    exit()

print(f"{first_number} + {second_number} = {first_number + second_number}")
print(f"{first_number} - {second_number} = {first_number - second_number}")
try:
    print(f"{first_number} / {second_number} = {first_number / second_number}")
except:
    print("Error: division by zero")
print(f"{first_number} * {second_number} = {first_number * second_number}")