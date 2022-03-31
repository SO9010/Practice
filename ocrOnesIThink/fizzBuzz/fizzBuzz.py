#!/usr/bin/env python
def main():
    for i in range(usrInput):
        i += 1 
        print(i,"", end="")
        #If you want to add another one use the same format, add it under here just uncomment it and you will see how it works
        #print(checkAgainst(i, 7, "Example"), end="")
        
        print(checkAgainst(i, 3, "fizz"), end="")
        print(checkAgainst(i, 5, "Buzz"))

def checkAgainst(currentNumber, number, name):
    if currentNumber % number == 0: #if 0 it means there is a full division
        return name
    else:
        return ""

usrInput = int(input("Please enter your number: "))
main()
