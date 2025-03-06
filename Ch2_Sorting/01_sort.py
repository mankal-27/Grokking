'''
sort an array from smallest to largest. Let’s write a function
to find the smallest element in an array
'''

def findSmallest(arr):
    smallest = arr[0] # Stores the smallest value
    smallest_index = 0 # Index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr): # Selection Sort|| O(n^2) || Sorts an array
    newArr = []
    copiedArr = list(arr) # Copy Array before mutating

    for i in range(len(arr)):
        smallest = findSmallest(copiedArr) # Find the smallest in tha array and adds it to the new array
        newArr.append(copiedArr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))