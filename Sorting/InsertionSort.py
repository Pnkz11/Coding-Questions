'''
Insertion sort almost sorts on o(n).
However, woerst is O(n)
'''

class InsertionSort():
	def __init__(self):
		pass

	def sort(self, values):
		self.insertionsort(values)

	def insertionsort(self, ar):
		'''
	    Sort the given array using insertion sort. The idea behind
	    insertion sort is that at the array is already sorted from
	    [0, i] and you want to add the element at position i+1, so
	    you 'insert' it at the appropriate location.   
	    '''

		if ar == None:
			return

		for i in range(1, len(ar)):
			j=i
			while j > 0 and ar[j] < ar[j-1]:
				self.swap(ar, j-1 , j)
				j -= 1

	def swap(self, ar, i , j):
		tmp = ar[i]
		ar[i] = ar[j]
		ar[j] = tmp

if __name__=='__main__':
	array = [2,-5, 64,3,43,4,5, 43,23, 32,4]
	sorter =InsertionSort()
	sorter.sort(array)
	print(array)


