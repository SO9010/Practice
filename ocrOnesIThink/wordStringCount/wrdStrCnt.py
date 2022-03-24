#!/usr/bin/env python

strOfFile = input("Please put in the text that you want to put in, if its a file please enter  FILE  : ")
strOfFile = strOfFile.strip()

if strOfFile == "FILE":
    fileLoc = input("Please input file name: ") #file should already be in the same folder but i could implemt to be where ever
    strOfFile = open(fileLoc)

totalWords = len(strOfFile.read().split())

print("There are", totalWords, "Total words press enter to continue.")