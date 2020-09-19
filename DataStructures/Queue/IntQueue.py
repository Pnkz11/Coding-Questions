'''
This file contains implementation of Interger only Queue
'''

import time
from array import array as arr
from collections import deque
from Queue import Queue

class IntQueue(Queue):
	'''
	An Integer only Q
	'''

	def __init__(self, maxSize):
		'''
		maxSize is the maximum number of items
		that can be in the queue at any given time
		'''
		self.front = 0
		self.end = 0
		self.qsize = 0
		self.data = arr('i', (0 for i in range (maxSize)))

	def size(self):
		'''
		return number of elements in the Queue
		'''
		return self.qsize

	def isEmpty(self):
		'''
		check if the Queue is empty
		'''
		return self.size == 0
    
	def isFull(self):
		'''
		Check if the Queue is Full
    	'''
		self.qsize == len(self.data)

	def peek():
		'''
    	Return the element from the front of the Queue
    	Throw error for empty queue
    	'''
		if isEmpty():
			raise Exception('Queue Empty')

		self.front = self.front % len(self.data)
		return self.data[self.front]

	def offer(self, value):
		'''
		Add an element to the queue
		'''
		if self.isFull():
			raise Exception('Queue too small')

		self.data[self.end] = value
		self.end += 1
		self.qsize += 1
		self.end = self.end % len(self.data)

	def poll(self):
		'''
		Make sure to check the queue is not empty before polling(removing element)
		'''
		if self.isEmpty():
			raise Exception('Empty Queue')

		self.qsize -= 1
		self.front = self.front % len(self.data)
		elem = self.data[self.front]
		self.front += 1

		return elem


def benchMarkTest():
		'''
		BenchMark IntQueue vs ArrayDeque
		'''

		n = 1000000
		intQ = IntQueue(n)

		#IntQueue time 
		start = time.process_time()

		for i in range(0, n):
			intQ.offer(i)
		for i in range(0, n):
			intQ.poll()

		end = time.process_time()
		print("IntQueue :", (end - start))


		#ArrayDeque times at around 1.1875 seconds
		arrayDeque = deque()
		start = time.process_time()
		
		for i in range(0, n):
		    arrayDeque.append(i)
		for i in range(0, n):
		    arrayDeque.popleft()
		
		end = time.process_time()
		print("ArrayDeque Time: ", (end - start))

if __name__ == '__main__':
	"""
	Example usage
	"""

	q = IntQueue(5)

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

	q.offer(1);
	q.offer(2);
	q.offer(3);

	print(q.poll()) # 5
	print(q.poll()) # 1
	print(q.poll()) # 2
	print(q.poll()) # 3

	print(q.isEmpty()) # true

	benchMarkTest()

	  		



