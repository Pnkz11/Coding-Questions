'''
Binary Search Implemetation 
O(log n)
'''

#import math

class BinarySearch():

	def __init__(self):
		pass

	def rec_binarySearch(self, ar, lo, hi, target):
		if hi <= lo:
			raise Exception("High shoud be greater than Low")

		mid = 0
		while True:
			#Find the mid point 
			mid = (lo + hi) // 2

			#If mid is the taget element
			if ar[mid] == target:
				return mid

			#If the element is smaller than mid, then recurse the left subarray
			elif ar[mid] > target:
				return self.binarySearch(arr, lo, mid -1, target)
			else:
				return self.binarySearch(arr, mid+1, hi, target)

		return -1

	def iter_binarySearch(self, ar, lo, hi, target):
		if hi <= lo:
			raise Exception("High shoud be greater than Low")

		while lo <= hi:
			mid = (lo + hi)//2
			if ar[mid] == target:
				return mid
			elif ar[mid] > target:
				hi = mid - 1
			else:
				lo = mid + 1
		#If element not fond, then return -1
		return -1


if __name__=='__main__':
	array = [4,6,7,9,10,45,234,546]
	sorter = BinarySearch()
	result = sorter.iter_binarySearch(array, 0, len(array)- 1, 9) + 1
	print("Found at Index:", result)








