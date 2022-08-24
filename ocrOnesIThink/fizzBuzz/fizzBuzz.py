#!/usr/bin/env python
singleCheck = 0
def main():
    for i in range(usrInput):
        i += 1 
        global singleCheck
        #If you want to add another one use the same format, add it under here just uncomment it and you will see how it works
        #example = checkAgainst(i, 7, "Example")
        fizz = checkAgainst(i, 3, "fizz")
        buzz = checkAgainst(i, 5, "Buzz")
        if singleCheck != 1:
            print(i,"", end="")
        #for the example to output the answer you have to uncomment below too 
        #print(example, end="")    
        print(fizz, end="")
        print(buzz)
        singleCheck = 0

def checkAgainst(currentNumber, number, name):
    if currentNumber % number == 0: #if 0 it means there is a full division
        global singleCheck
        singleCheck += 1
        return name
    else:
        return ""

usrInput = int(input("Please enter your number: "))
main()
