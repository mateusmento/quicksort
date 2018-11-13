from random import randint

def quicksort(arr, ini, fim):
	if ini < fim:
		pp = partition(arr, ini, fim)
		quicksort(arr, ini, pp)
		quicksort(arr, pp+1,fim)
	return arr

def partition(arr, ini, fim):
	pivo = arr[fim-1]
	start = ini
	for i in range(ini,fim):
		if arr[i] <= pivo:
			start += 1
			swap(arr, start-1, i)
	return start-1
	
def randpartition(arr,ini,fim):
	rand = randint(ini,fim)
	swap(arr, rand, fim-1)
	return partition(arr,ini,fim)

def swap(arr, a, b):
	arr[a], arr[b] = arr[b], arr[a]

arr = [8,5,12,55,3,7,82,44,35,25,41,29,17]
print (arr)
print (quicksort(arr,0,len(arr)))


