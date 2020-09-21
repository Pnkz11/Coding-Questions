'''
Quick Sort Implementation
Based on the splitting of an array (partition) into smaller ones 
and swapping (exchange) based on the comparison with 'pivot' element selected. 
Due to this, quick sort is also called as "Partition Exchange" sort. 
Like Merge sort, Quick sort also falls into the category of divide and conquer approach of problem-solving methodology.
'''

import sys

class QuickSort():

	def __init__(self):
		pass

	def sort(self, values):
		if values == None:
			return
		return self.quickSort(values, 0, len(values) - 1)

	def quickSort(self, ar, lo, hi):
		'''
		Sort interval [lo,hi] inplace recursively
		low --> Starting index, high --> Ending index
		'''
		if lo < hi:
			# pi is partitioning index, ar[pi] is now at right place
			splitPoint = self.partition(ar, lo, hi)
			self.quickSort(ar, lo, splitPoint -1 ) #Before pi
			self.quickSort(ar, splitPoint +1, hi)  #After pi

	def partition(self, ar, lo, hi):
		'''
		Performs Hoare partition algorithm for quicksort.
		This function takes last element as pivot, 
		places the pivot element at its correct position in sorted array, 
		and places all smaller (smaller than pivot) to left of pivot 
		and all greater elements to right of pivot     
    	'''
    	#Pivot (Element to be placed at right position)
    	pivot = ar[hi]
    	i = lo - 1 #Index of the samller element 

    	for j in range(lo, hi):
    		#If element is smaller than the pivot 
    		if ar[j] < pivot:
    			i += 1 #Increment the index of the smaller element 
    			self.swap(ar, i, j)

    	self.swap(ar, i+1, hi)

    def swap(self, ar, i, j):
    	tmp = ar[i]
    	ar[i] = ar[j]
    	ar[j] = tmp


if __name__='__main__':
	array = [3,5,2,3,5,34,77,9,35]
	sorter = QuickSort()
	sorter.sort(array)
	print(array)









