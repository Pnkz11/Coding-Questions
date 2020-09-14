#Given an array of integers find the kth element in the sorted order (not the kth distinct element). 
#So, if the array is [3, 1, 2, 1, 4] and k is 3 then the result is 2, because it’s the 3rd element 
#in sorted order (but the 3rd distinct element is 3).

#Sort Array and print kth, The complexity is NlogN where N is size of the array
def kthElement_sortArray(arr, k):
	arr.sort()
	if k <= len(arr):
		print(arr[k])

#Selction algorithm (quick sort  Av. time 0(N)  &  worst time 0(N^2))
def partition1(arr, left, right, pivotIndex):
	arr[right], arr[pivotIndex] = arr[pivotIndex], arr[right]
	pivot = arr[right]
	swapIndex=left
	breakpoint()
	for i in range(left, right):
		if arr[i] <  pivot:
			arr[i], arr[swapIndex] = arr[swapIndex], arr[i]
			swapIndex += 1
	arr[right], arr[swapIndex] =  arr[swapIndex], arr[right]
	return swapIndex

import random
def kthLargest1(arr, left, right, k):
	if not 1<=k<=len(arr):
		return
	if left == right:
		return arr[left]
	#breakpoint()
	while True:
		pivotIndex = random.randint(left, right)
		pivotIndex = partition1(arr, left, right, pivotIndex)
		rank = pivotIndex -left + 1

		if rank == k:
			return arr[pivotIndex]
		elif k < rank:
			return kthLargest1(arr, left, pivotIndex-1, k)
		else:
			return kthLargest1(arr,pivotIndex+1 , right, k-rank)

# Using Median of Medians Algorithm. 0(N)

def partition2(arr, left, right, pivot):
	swapIndex=left
	for i in range(left, right):
		if arr[i] <  pivot:
			arr[i], arr[swapIndex] = arr[swapIndex], arr[i]
			swapIndex += 1
	return swapIndex-1

def kthLargest2(arr, left, right, k):
	length =  right - left +1
	if not 1<=k<=length:
		return

	if length <=5:
		return sorted(arr[left:right+1])[k-1]

	numMedians = length//5
	#breakpoint()
	medians = [kthLargest2(arr, left+5*i, left+5*(i+1)-1, 3) for i in range(numMedians)]
	pivot=kthLargest2(medians, 0 , len(medians)-1, len(medians)//2+1)
	#breakpoint()
	pivotIndex = partition2(arr, left, right, pivot)

	rank=pivotIndex-left+1
	if k <= rank:
		return kthLargest2(arr, left, pivotIndex, k)
	else:
		return kthLargest2(arr, pivotIndex+1, right, k-rank)



if __name__ == '__main__':
	arr=[1, 11, 21, 2, 12, 22, 13, 13, 23, 4, 14, 24, 5, 15, 25]
	result = kthLargest2(arr, 0, (len(arr))-1, 9)
	print(result)
