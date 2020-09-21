def findTriplet(arr, n):
	arr.sort()

	i = n- 1 #last element

	while i>=0:
		k = i-1
		j = 0
		while (j<k):
			if (arr[i] == arr[j] + arr[k]): 
				#pair found
				return[arr[i], arr[j], arr[k]]

			elif (arr[i] > arr[j] + arr[k]):
				j +=1

			else: 
				k -= 1
		i -= 1
	return -1

if __name__=='__main__':
	arr = [2,4, 5, 7,3,43,21,28]
	print(findTriplet(arr, len(arr)))





