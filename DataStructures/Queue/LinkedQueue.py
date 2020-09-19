'''
Linked list implementation of Queue
'''

from Queue import Queue
from DoublyLinkedList import DoublyLinkedList

class LinkedQueue(Queue):
	'''
	A linked list implementation of Queue
	'''
	def __init__(self):
		self.list = DoublyLinkedList()
		self.iterList = iter(self, list)

	def size(self):
		'''
		Return the size of the queue
		'''
		return self.list.size()

	def isEmpty(self):
		'''
		Return if Queue is Empty
		'''
		return self.size() == 0

	def peek(self):
		'''
		This method allows looking at the front of the Queue 
		Throws error if Queue is empty
		'''
		if self.isEmpty():
			raise Exception('Empty Queue')

		return self.list.peekFirst()

	def poll(self):
		'''
		Dequeue/Remove an element from the front of the Queue
		'''
		if isEmpty():
			raise Exception('Empty Queue')

		return self.list.removeFirst()
	
	def offer(self, elem):
		'''
		Enqueue/Add an element at the end of the queue
		'''
		return self.list.addLast(elem)

	def __iter__(self):
		'''
		callled when iteratir is initiallized

		return an iterator to allow the user to traverse
		through the elements found inside the queeue
		'''
		self.iterList = iter(self.list)
		return self

	def __next__(self):
		'''
		To move to next element
		'''
		return  next(self.iterList)


	if __name__=='__main__':
		q = LinkedQueue()
		q.offer(1)
		q.offer(2)
		q.offer(3)
		q.offer(4)
		q.offer(5)

		print(q.poll()) # 1
		print(q.poll()) # 2
		print(q.poll()) # 3
		print(q.poll()) # 4

		print(q.isEmpty()) # false

		q.offer(1)
		q.offer(2)
		q.offer(3)

		print(q.poll()) # 5
		print(q.poll()) # 1
		print(q.poll()) # 2
		print(q.poll()) # 3

		print(q.isEmpty()) # true






