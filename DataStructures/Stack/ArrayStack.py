'''
Array implementation of Stack
'''

import sys
from Stack import Stack

class ArrayStack(Stack):
	'''
	An Array implementation of Stack
	'''

	def __init__(self, obj):
		self.stackSize=0
		self.data = []
		self.initSize = sys.getsizeof(self.data)


	def size(self):
		return self.stackSize

	def isEmpty(self):
		return self.stackSize == 0

	def push(self, elem):
		self.data.append(elem)
		self.stackSize +=1
		spaceLeft = ((sys.getsizeof(self.data) - self.initSize) - len(self.data) * 8) // 8
		print("'sapce left after append: " , spaceLeft)

	def pop(self):
		if self.isEmpty():
			raise Exception('Empty Stack')
		self.stackSize -=1
		elem = self.data[self.stackSize]

		return elem

	def peek(self):
		if isEmpty():
			raise Exception('Empty Stack')

		return self.dat[self.stackSize -1]

if __name__=='__main__':
	'''
	Example usage
	'''

	s = ArrayStack(5)
	s.push(1)
	s.push(2)
	s.push(3)
	s.push(4)
	s.push(5)

	print(s.pop()) # 5
	print(s.pop()) # 4
	print(s.pop()) # 3

	s.push(3)
	s.push(4)
	s.push(5)

	while s.isEmpty() is False:
	    print(s.pop())


