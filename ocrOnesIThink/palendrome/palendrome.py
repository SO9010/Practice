#!/usr/bin/env python

word = input("Please enter the word: ")
isPalendrome = True
endOfStringToCheck = len(word) -1 
for i in range(int(len(word)/2)):
    if word[i] != word[endOfStringToCheck]:
        isPalendrome = False
        break
    endOfStringToCheck += -1 
print("Is it a panendrome...", isPalendrome)
