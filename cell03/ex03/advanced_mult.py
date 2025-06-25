#!/usr/bin/env python3
base_number = 0
while base_number < 11:
    print(f"Table de {base_number}:", end=" ")
    multiplication_number = 0
    while multiplication_number < 11:
        total = base_number * multiplication_number
        print(f"{total}", end=" ")
        multiplication_number += 1
    base_number += 1
    print("")