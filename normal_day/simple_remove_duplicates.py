def solve(arr):
	for i in range(0,len(arr)):
		temp = arr.remove(arr[i])
		print(temp)
		#if arr[i] in temp:
		#	result = arr.pop(i)
	#return result

alist = [3, 4, 4, 3, 6, 3]
solve(alist)