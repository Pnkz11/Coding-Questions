def LCS(arr):
	if len(arr)==0:
		return
	currentSum=maxSum=arr[0]
	
	for num in arr[1:]:
		currentSum = max(currentSum+num, num)
		maxSum = max(currentSum, maxSum)
	return maxSum

def LCS_start_end(arr):
	if len(arr)==0:
		return 0

	currentSum=maxSum=arr[0]
	start=tstart=end=0

	for pos in range(1, len(arr)):
		if (arr[pos] > currentSum+arr[pos]):
			currentSum=arr[pos]
			tstart=pos
		else:
			currentSum+=arr[pos]

		if currentSum>maxSum:
			maxSum = currentSum
			start=tstart
			end=pos
	return maxSum, start,end

if __name__ == '__main__':
	arr=[2,4,-4,3,-2,0,1]
	#maxSum=LCS(arr)
	maxSum, start,end= LCS_start_end(arr)
	print(maxSum, start,end)
	#print(maxSum)