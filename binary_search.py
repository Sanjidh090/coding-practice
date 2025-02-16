def search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2 # make sure to round it down
        if arr[mid] == target:
	        return mid
        elif target < arr[mid]:
	        right = mid - 1
        else:
            left = mid + 1
    return f"not found"

arr1 = [-2, 3, 4, 7, 8, 9, 11, 13]
assert search(arr1, 11) == 6
assert search(arr1, 13) == 7

arr2 = [3]
assert search(arr2, 6) == -1
assert search(arr2, 2) == -1
assert search(arr2, 3) == 0
print(f"Results: {search(arr1, 11)}, {search(arr1, 13)}, {search(arr2, 6)}, {search(arr2, 2)}, {search(arr2, 3)}")
