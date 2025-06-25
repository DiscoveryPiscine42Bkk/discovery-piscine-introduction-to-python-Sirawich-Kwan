#!/usr/bin/env python3

enter_word = input("Enter your word: ")
new_word = ""
for character in enter_word:
    if character.isupper():
        character = character.lower()
        new_word += character
    else:
        character = character.upper()
        new_word += character
print(new_word)