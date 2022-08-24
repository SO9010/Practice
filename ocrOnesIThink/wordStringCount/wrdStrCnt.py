#!/usr/bin/env python

strOfFile = input("Please put in the text that you want to put in, if its a file please enter  FILE  : ")
strOfFile = strOfFile.strip()

if strOfFile == "FILE":
    fileLoc = input("Please input file name: ") #file has to be in same loc 
    strOfFile = open(fileLoc)

totalWords = len(strOfFile.read().split()) #Uses spaces to split into array
print("There are", totalWords, "Total words.") 