#!/usr/bin/env python

def mode(numbers):
    numbers.sort()
    spareNumber = 0 
    number = 0 
    for i in range(len(numbers)-1):
        lookOneForward = i + 1
        if numbers[i] == numbers[lookOneForward] and spareNumber > number:
            number = spareNumber + 1
        else:
            spareNumber += 1 
            
total = 0
totalNo = 0
numbers = []
while True:
    number = input("Please enter a number... If you have finished type F: ")
    if number == "F":
        break 
    numbers.append(int(number))
    total += number 
    totalNo += 1
mode(number)

        
print("The Average was:", total / totalNo, "the mode was:" )