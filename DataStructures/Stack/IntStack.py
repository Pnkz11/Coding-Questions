'''
A sample Integer stack which is quick and lightwieght
'''

import time
from collections import deque
from queue import LifoQueue
from ListStack import ListStack
from ArrayStack import ArrayStack
from array import array as arr
from Stack import Stack


class IntStack(Stack):
	'''
	An Integer implementation of a Stack
	'''

	def __init__(self, maxSize):
		'''
		maxSize is the maximium capacity of the stack
		'''
		self.pos = 0
		self.ar = arr('i' (0 for i in range(maxSize)))


	def size(self):
		'''
		Returns the number of elements inside the Stack
		'''
		return self.pos

	def isEmpty(self):
		'''
		Return True/False on whether stack is Empty
		'''
		return self.pos == 0

	def peek(self):
		'''
		Add the element from top of the Stack
		Else, throw error if stack is Empty
		'''
		if self.isEmpty():
			raise Exception('Empty Queue')

		return self.ar[self.pos - 1 ]


	def push(self,value):
		'''
		Push an element in the stack.
		Throw error if stack is full
		'''
		if self.self.pos == maxSize:
			rasie Exception('Stack Full')

		self.ar[self.pos] = value
		self.pos += 1
	
	def pop(self):
		'''
		Return the top element Stack 
		throw error if stack empty 
		'''
		if self.isEmpty():
			raise Exception('stack empty')

		self.pos -= 1
		return self.ar[self.pos]

	def benchMarkTest():
		'''
		BenchMark IntStack vs Pythin Deque
		'''
		n = 1000000
		intStack = IntStack(n)

		#Implementation using IntStack Module
		start = time.process_time()

		for i in range(0, n):
			intStack.push(i)
		for i in range(0, n):
			intStack.pop()

		end = time.process_time()
		print("IntStack Time : ", (end-start))


		#Implementation using ListStack Module
		listStack = ListStack()
		start = time.process_time()

		for i in range(0, n):
			listStack.push(i)
		for i in range(0, n):
			listStack.pop()

		end = time.process_time()
		print("ListStack Time : ", (end-start))


		#Implementation using ArrayStack Module
		arrayStack = ArrayStack()
		start = time.process_time()

		for i in range(0, n):
			arrayStack.push(i)
		for i in range(0, n):
			arrayStack.pop()

		end = time.process_time()
		print("ArrayStack Time : ", (end-start))



	    # Implementation using collections.deque
	    # Python stack can be implemented using deque class from collections module. 
		# Deque is preferred over list in the cases where we need quicker append and 
		# pop operations from both the ends of the container, as deque provides an O(1) 
		# time complexity for append and pop operations as compared to list which 
		# provides O(n) time complexity.
		# Same methods on deque as seen in list are used, append() and pop().
		stackDeque = deque()
		#deque are slower when you give initial capacity
		start = time.process_time()

		for i in range(0, n):
			stackDeque.append(i)
		for i in range(0, n):
			stackDeque.pop()

		end = time.process_time()
		print("StackDeque Time : ", (end-start))


  		# Implemenation using queue module (33.765625 sec)
  		# Queue module also has a LIFO Queue, which is basically a Stack. Data is 
  		# inserted into Queue using put() function and get() takes data out from the Queue.

		lifoStack = LifoQueue(maxsize = n)
		start = time.process_time()

		for i in range(0, n):
			lifoStack.put(i)
		for i in range(0, n):
			lifoStack.get()

		end = time.process_time()
		print("LIFOStack Time : ", (end-start))


	if __name__ == '__main__':
	    """
	    Example usage
	    """

	    s = IntStack(5)

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

	    benchMarkTest()






