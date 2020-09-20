'''
Bubble sort implememtation ==> Not very efficient sorting technique.
Normally, one should avoid it. 
'''

class BubbleSort():

	def __init__(self):
		pass


	def sort(self, ar):
		'''
		Sort the array using bubble sort. The idea behind the bubble sort is:
		To look for adjacent indexes which are out of order and interchange thier 
		element until the entore array is sorted
		'''
		if ar == None:
			return

		sorted=False
		while True:
			sorted = True
			for i in range(1, len(ar)):
				if ar[i] < ar[i-1]:
					self.swap(ar,i-1, i)
					sorted = False
			if sorted:
				break

	def swap(self, ar, i, j ):
		tmp = ar[i]
		ar[i] = ar[j]
		ar[j] = tmp


if __name__=='__main__':
	'''
	Example usage 
	'''
	array =[9,54,6,43,23,12,0,98]
	sorter = BubbleSort()
	sorter.sort(array)
	print(array)




