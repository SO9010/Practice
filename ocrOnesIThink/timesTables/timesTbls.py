#!/usr/bin/env python
numberToTimesBy = int(input("Please enter the number you want to get multiplied: ")) 
howManyTimes = int(input("please enter the amount of times to have this multiplied: "))
for i in range(howManyTimes):
    print(numberToTimesBy, "X", i, "=", numberToTimesBy * i)