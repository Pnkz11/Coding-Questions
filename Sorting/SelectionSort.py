'''
Selection sort Algorithm. O(n^2)

'''

class SelectionSort():

	def __init__(self):
		pass

	def sort(self, values):
		if values == None:
			return
		return self.selectionSort(values)


	def selectionSort(self, array):

		N = len(array)

		for i in range(0, N):
			#Find the index beyond i woth a lower valuse than i
			swapIndex = i
			for j in range(i+1, N):
				if array[j] < array[swapIndex]:
					swapIndex = j

			self.swap(array, i, swapIndex)

	def swap(self, ar, i , j):
		tmp = ar[i]
		ar[i] = ar[j]
		ar[j] = tmp

if __name__=='__main__':
	array = [2,-5, 64,3,43,4,5, 43,23, 32,4]
	sorter =SelectionSort()
	sorter.sort(array)
	print(array)


