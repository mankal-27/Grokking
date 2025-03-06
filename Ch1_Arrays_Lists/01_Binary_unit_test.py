import unittest

def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

class TestBinarySearch(unittest.TestCase):
    def test_found(self):
        arr = [1, 3, 5, 7, 9]
        item = 3
        self.assertEqual(binary_search(arr, item), 1)

    def test_not_found(self):
        arr = [1, 3, 5, 7, 9]
        item = -1
        self.assertIsNone(binary_search(arr, item))

    def test_empty_array(self):
        arr = []
        item = 3
        self.assertIsNone(binary_search(arr, item))

    def test_single_element_array_found(self):
        arr = [3]
        item = 3
        self.assertEqual(binary_search(arr, item), 0)

    def test_single_element_array_not_found(self):
        arr = [3]
        item = -1
        self.assertIsNone(binary_search(arr, item))

    def test_large_array(self):
        arr = list(range(1000))
        item = 500
        self.assertEqual(binary_search(arr, item), 500)

if __name__ == '__main__':
    unittest.main()