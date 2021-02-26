def binary_search(arr, low, high, x):
	if high >= low:
		mid = (low+high)//2

		if arr[mid] == x:
			return mid

		elif arr[mid] > x:
			return binary_search(arr, low, mid-1, x)
		else:
			return binary_search(arr, mid+1, high, x)

	else:
		return -1



array = [1, 4,  6, 9, 10]
x = 4

result = binary_search(array, 0, len(array)-1, x)

if result != -1:
	print("Index of element is ", str(result))
else:
	print("Not found!")