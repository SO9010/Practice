#!/usr/bin/env python
def squared(userInput):
    for i in range(userInput):
        print(i+1, "Squared is", str((i+1)*(i+1)))

userInput = int(input("Please enter a number: "))
squared(userInput)
