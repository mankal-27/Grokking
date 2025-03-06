'''
Write a recursive function to dd count the number of
items in a list.
'''

def count(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + count(arr[1:])

print(count([1, 2, 3, 4, 5]))