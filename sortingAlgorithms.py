#sortingAlgorithms
#Filip Rokita
#www.filiprokita.com

import random

arr = []
for i in range(10000):
    arr.append(random.randint(0, 9))

def bubbleSort(array):
    n = len(array)
    for i in range(n):
        alreadySorted = False
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                alreadySorted = False
            if alreadySorted == True: break
    return array

def insertionSort(array):
    n = len(array)
    for i in range(n):
        keyItem = array[i]
        j = i - 1
        while j >= 0 and array[j] > keyItem:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = keyItem
    return array

print("Bubble Sort: ", bubbleSort(arr))
print("Insertion Sort: ", insertionSort(arr))