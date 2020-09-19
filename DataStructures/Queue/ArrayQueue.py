'''
An array implementation of a queue
'''

from Queue import Queue

class ArrayQueue(Queue):
	'''
	Array implemetation of Queue
	'''
	def __init__(self, obj, capacity):
		self.qSize = 0 
		self.data = [obj for i in range(capacity)]
		self.front = 0
		self.rear = 0

	def adjustIndex(self, index, size):
		return index - size if index >= size else index

	def size(self):
		return self.adjustIndex(self.rear + len(self.data) - self.front , len(self.data))

	def isFull(self):
		return (self.front + len(self.data) - self.rear) % len(self.data) == 1

	def isEmpty(self):
		return self.front == self.rear


	def offer(self, elem): # enqueue or adding
		if self.isFull():
			raise Exception('Queue is Full')
		self.data[self.rear]=elem
		self.rear += 1
		self.rear = self.adjustIndex(self.rear, len(self.data))

	def poll(self): #dequeue oe remove from 1st
		if self.isEmpty():
			raise Exception('Queue is Empty')

		self.front = self.adjustIndex(self.front, len(self.data))
		data = self.data[self.front]
		self.front +=1
		
		return data

	def peek(self):
		if self.isEmpty():
			raise Exception('Queue is Empty')
		self.front = self.adjustIndex(self.front, len(self.data))

		return self.front


if __name__ == '__main__':
	q = ArrayQueue(0, 6)

	q.offer(1);
	q.offer(2);
	q.offer(3);
	q.offer(4);
	q.offer(5);

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





