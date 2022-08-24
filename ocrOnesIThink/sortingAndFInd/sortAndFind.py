#!/usr/bin/env python

#bubble sort sticks with the same number untill its in the correct space


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
        swapPlace = 0
        check = 1
        tmp = 0 #tempory hold for swap
        for index in range(1, len(arr)-1, 1):
            print(index)
            for check in range(index, swapPlace, -1):
                
                if arr[index] < arr[check]:
                    print(arr[check])

                    swapPlace = check
                    break
        return arr 
arr = [5,4,2,3,123,2,1]
print(insertionSort(arr, sorted))