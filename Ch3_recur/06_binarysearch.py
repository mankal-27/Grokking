'''
Remember binary search from chapter 1? It’s a
divide-and-conquer algorithm, too. Cddan you come up
with the base case and recursive case for binary
search?
'''

def binary_search(arr, item):
    if len(arr) == 0:
        return None
    else:
        mid = len(arr) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            return binary_search(arr[mid+1:], item)
        else:
            return binary_search(arr[:mid], item)

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))