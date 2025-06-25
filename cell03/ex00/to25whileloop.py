#!/usr/bin/env python3
start_number = input("Enter a number less than 25\n")
try:
    start_number = int(start_number)
except:
    print("The input isn't number")
    exit()

if start_number > 25:
    print("Error")
    exit()
else:
    while start_number <= 25:
        print(f"Inside the loop, my variable is {start_number}")
        start_number += 1
