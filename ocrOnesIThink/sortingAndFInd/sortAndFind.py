#!/usr/bin/env python

#bubble sort sticks with the same number untill its in the correct space
from numpy import array


sorted = False
def bubbleSort(arr, sorted):
    fullCheck = 0
    while sorted != True:
        check = 1
        tmp = 0 #tempory hold for swap
        for index in range(0, len(arr)-1, 1):
            if arr[index] > arr[check]:
                tmp = arr[check]
                arr[check] = arr[index]
                arr[index] = tmp
            if fullCheck == len(arr)-1:
                sorted = True 
                break
            check += 1
        fullCheck += 1
    return arr

def insertionSort(arr, sorted):
    while sorted != True:
        check = 1
        tmp = 0 #tempory hold for swap
        for index in range(0, len(arr)-1, 1):
            for check in range(0, len(arr)-1, 1):
                if arr[index] > arr[check] 
arr = [5,4,2,3,123,2,1]
print(bubbleSort(arr, sorted))