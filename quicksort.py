from random import randint

swp_count = 0
ifs_count = 0

def quicksort(arr, beg, end, separateFn):
	global ifs_count
	if beg < end:
		ifs_count += 1
		pivot = separateFn(arr, beg, end)
		quicksort(arr, beg, pivot - 1, separateFn)
		quicksort(arr, pivot + 1, end, separateFn)
	return arr

def quicksort1(arr, beg, end):
	return quicksort(arr, beg, end, lambda a,b,e : separate(a,b,e,randint(b,e)))

def quicksort2(arr, beg, end):
	return quicksort(arr, beg, end, lambda a,b,e : separate(a,b,e,b))

def separate(arr, beg, end, pos):
	global ifs_count
	msg = "ANTES: " + str(arr) + " PIVO: " + str(arr[pos])
	pivot = arr[pos]
	left = beg
	right = end
	while left < right:
		while left < end and arr[left] <= pivot:
			ifs_count += 1
			left += 1

		while right > beg and arr[right] > pivot:
			ifs_count += 1
			right -= 1

		if left < right:
			ifs_count += 1
			swap(arr, left, right)

	new_pos = -1
	if pos <= right:
		ifs_count += 1
		new_pos = right
	else:
		new_pos = left

	swap(arr, pos, new_pos)
	print (msg + " DEPOIS: " + str(arr))
	return new_pos

def swap(arr, left, right):
	global swp_count
	swp_count += 1
	arr[left], arr[right] = arr[right], arr[left]


arr = ['J', 'O', 'A', 'V', 'I', 'C', 'T', 'R', 'F', 'L', 'E', 'S', 'D', 'U', 'N', 'H', 'G', 'M', 'P', 'Y']

num = input("input: ")
if num == '1':
	quicksort1(arr, 0, len(arr)-1)
elif num == '2':
	quicksort2(arr, 0, len(arr)-1)
else:
	print ('wrong input')

print ('contagem de comparações: ' + str(ifs_count))
print ('contagem de trocas: ' + str(swp_count))
