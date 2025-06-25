#!/usr/bin/env python3
input_number = input("Enter a number\n")
try:
    input_number = int(input_number)
except:
    print(f"{input_number} isn't a number")
    exit()
times = 0
while times < 10:
    total = times * input_number
    print(f"{times} x {input_number} = {total}")
    times += 1