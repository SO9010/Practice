#!/usr/bin/env python
vowls = {"a":0, "e":0, "i":0, "o":0, "u":0}

text = input("Please enter the text: ")
for index in text:
    if index == "a":
        vowls["a"] += 1
    elif index == "e":
        vowls["e"] += 1
    elif index == "i":
        vowls["i"] += 1
    elif index == "o":
        vowls["i"] += 1
    elif index == "u":
        vowls["u"] += 1
total = vowls["a"] + vowls["e"] + vowls["i"] + vowls["o"] + vowls["u"]#
print(vowls)
print("The total vowels is:", total)