'''
Write a recursive function to dd find the maximum
number in a list.
'''

def max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[1:])

print(max([1, 2, 3, 4, 10, 5, 6, 7, 8]))