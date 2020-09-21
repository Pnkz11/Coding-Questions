'''
MergeSort Implemtation
0(nlog n)
'''

import sys

class MergeSort():
	'''
	MergeSort Implements InplaceSort for the ease of testing,
	but in reality it is not really good for an inplace sorting algorithm
	'''

	def __init__(self):
		pass

	def sort(self, values):
		return self.mergeSort(values)

	def mergeSort(self, ar):
		'''
		Base case is when a single element is left(which is already sorted)
		'''
		n = len(ar)
		if n <= 1:
			return ar

		#Split the array into half and recursively sort them 
		left = self.mergeSort(ar[:n//2])
		right = self.mergeSort(ar[n//2::])

		#Combine the two arrays into one large array
		return self.merge(left, right)

	def merge(slef, ar1, ar2):
		'''
		Merge two sorted arrays into a large array
		'''
		n1 = len(ar1)
		n2 = len(ar2)
		n = n1 + n2
		i1 = 0
		i2 = 0
		ar = [0]*n

		for i in range(0, n):
			if i1 == n1:
				ar[i] = ar2[i2]
				i2 += 1
			elif i2 == n2:
				ar[i] =  ar1[i1]
				i1 += 1
			else:
				if ar1[i1] < ar2[i2]:
					ar[i] = ar1[i1]
					i1 += 1
				else:
					ar[i] = ar2[i2]
					i2 += 1 
		return ar

if __name__=='__main__':
	'''
	Example usage
	'''
	array = [3,54,3,-9,6,65,55,43,123,43,78]
	sorter = MergeSort()
	array = sorter.sort(array)
	print(array)






