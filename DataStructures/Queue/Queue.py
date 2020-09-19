'''
Abstract class for Queue
'''

from abc import ABC, abstractmethod

class Queue(ABC):

	@abstractmethod
	def offer(self, elem): # enqueue or adding
		pass

	@abstractmethod
	def poll(self): # dequeue or removing
		pass

	@abstractmethod 
	def peek(self):
	    pass

	@abstractmethod
	def size(self):
	    pass

	@abstractmethod
	def isEmpty(self):
	    pass
