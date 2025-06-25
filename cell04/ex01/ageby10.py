#!/usr/bin/env python3

input_age = input("Please tell me your age: ")
try:
    input_age = int(input_age)
except:
    print("Input isn't a number")
    exit()

print(f"You are currently {input_age} years old.")
for times in range(1, 4):
    print(f"In {times * 10} years, you'll be {input_age + (times * 10)} years old.")