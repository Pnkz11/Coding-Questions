'''
Stack implementation with Doubly linked list
'''


from Stack import Stack
from DataStructures.LinkedList.DoublyLinkedList import DoulbyLinkedList

class ListStack(Stack):
	'''
	A linked list implemetation of stack
	'''

	def __init__(self):
		self.list = DoulbyLinkedList()
		self.iterList = iter(self.list)


	def size(self):
		'''
		Ruturn the number of Itemin the stack
		'''
		self.list.size()

	def isEmpty(self):
		'''
		check if the Stack is empty
		'''
		return self.size() == 0

	def push(self, elem):
		'''
		Push element in the stack
		'''
		return self.list.addLast(elem)

	def pop(self):
		'''
		Pop an element off the stack
		Throw an error if the stack in empty
		'''
		if self.isEmpty():
			raise Exception('Empty Stack')

		return self.list.removelast()

	def peek():
		'''
		Peek the top of the stack wothour removing the element 
		Throw an error if the stack is empty
		'''
		if self.isEmpty():
			raise Exception('Empty stack')
		return self.list.peekLast()

	def __iter__(self):
		'''
		Called when iteration is initialized
		'''
		slef.iterList = iter(self.list)
		return self

	def __next__(self):
		'''
		to move to next element 
		'''
		return next(self.iterlist)

if __name__=='__main__':
	'''
	Example usage
	'''

	s = ListStack(5)
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

