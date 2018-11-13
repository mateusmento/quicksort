from random import randint

def quicksort(arr, beg, end):
	p = randint(beg, end)
	if beg < end:
		pivot = partition(arr, p, beg, end)
		quicksort(arr, beg, pivot - 1)
		quicksort(arr, pivot + 1, end)
		return arr

def partition(arr, p, beg, end):
	pivot_index = p
	pivot = arr[pivot_index]
	i = end
	for j in range(end, beg, -1):
		msg = str(arr) + " ---- (" + str(j) + ") " + str(i)
		if arr[j] > pivot:
			swap(arr, i, j)
			i -= 1
		msg += " => " + str(i) + " [" + str(pivot_index) + "]"
		print(msg)
	swap(arr, i, pivot_index)
	return i

def swap(arr, a, b):
	arr[a], arr[b] = arr[b], arr[a]


order = [0,1,2,3,4,5,6]
arr = [8,6,3,1,2,9,5]
print(order)
print ""
quicksort(arr, 0, len(arr) - 1)
print(arr)
