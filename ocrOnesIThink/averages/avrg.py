#!/usr/bin/env python
import string

total = 0
totalNo = 0
numbers = []

while True:
    number = input("Please enter a number... ")
    number.strip().lower()
    if number == "":
        break 
    numbers.append(int(number))
    total += int(number)
    totalNo += 1
    if total > 0: 
        average = total / totalNo

def mode(numbers):
    numbers.sort()
    spareNumber = 0 
    number = 0 
    indexOfChange = 0
    for i in range(len(numbers)-1):
        lookOneForward = i + 1
        if numbers[i] == numbers[lookOneForward] and spareNumber >= number:
            indexOfChange = i
        else:
            spareNumber += 1 
        number += 1
    return numbers[indexOfChange]

def midNumber(numbers):
    numbers.sort()
    midpoint = int(len(numbers)/2)
    return numbers[midpoint]

        
print("The Average was:", average, "the mode was:", mode(numbers), "the medean was:", midNumber(numbers))