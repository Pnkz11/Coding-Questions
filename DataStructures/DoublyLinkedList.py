 
 import ctypes

 class Node(object):
 	'''
 	Internal node class to represent data
 	'''
 	def __init__(self, data, prev, next)
 		self.data = data
 		self.prev = prev
 		self.next = next

 	def __repr__(self):
 		return str(self.data)

class DoulbyLinkedList(object):

	def __init__(self):
		self.llsize=0
		self.head =None
		self.tail=None
		self.travIter=None

	def __len__(self):
		return self.llsize

	def clear(self):
		'''
		Empty the linked list, 0(n)

		'''
		trav = self.head
		while trav is not None:
			next = trav.next
			trav.prev=trav.next= None
			trav.data = None
			trav = next

		self.head=None
		self.tail=None
		trav=None
		self.llsize=0

	def size(self):
		'''
		Return the size of the Linked List
		'''
		return self.llsize

	def isEmpty(self):
		'''
		Is the Linked List Empty
		'''
		return self.size() == 0

	def add(self, elem):
		'''
		Add an element to the tail of the Linked List, O(1) 
		'''
		self.addLast(elem)

	def addLast(self, elem):
		'''
		Add a NODE to the tail of the Linked List, O(1)
		'''
		#If the linked list is empty
		if self.isEmpty():
			self.head = self.tail = Node(elem, None, None)
		else:
			self.tail.next=Node(elem, self.tail, None)
			self.tail = self.tail.next

		self.llsize+=1


	def addFirst(self, elem):
		'''
		Add the element at the start of the Linked List, 0(1)
		'''
		#If the linked list is Empty
		if isEmpty():
			self.head = self.tail = Node(elem, None, None)
		else:
			self.head.prev = Node(elem, None, self.head)
			self.head = self.head.prev

		self.llsize+=1

	 def addAt(self, index, data):
	 	'''
	 	Add an element at a specific index
	 	'''
	 	if index < 0:
	 		raise Exception('Index should not be negative. The value of the Index was: {}'.format(index))

	 	if index == 0:
	 		self.addFirst(data)
	 		return

	 	if index==self.llsize:
	 		self.addLast(data)

	 	temp=self.head
	 	for i in range(0, index-1):
	 		temp=temp.next

	 	newNode = Node(data, temp, temp.next)
	 	temp.next=newNOde
	 	temp.next.prev=newNOde

	 	self.llsize+=1

	 def peekFirst(self):
	 	'''
	 	Check the 1st Node if it exists, O(1)
	 	'''
	 	if self.isEmpty():
	 		raise Exception('Empty List')
	 	return self.head.data

	 def peekLast(self):
	 	'''
	 	Check for tha Last Node, O(1)
	 	'''
	 	if self.isEmpty():
	 		raise Exception('Empty List')
	 	return self.tail.data

	 def removeFirst(self):
	 	'''
	 	Remove the First Node of the list, (1)
	 	'''
	 	#Can't remove an empty List
	 	if self.isEmpty():
	 		raise Exception('Empty List')

	 	'''
	 	Extract the data from the head
	 	And, move the head pionter to next Node
	 	'''
	 	data = self.head.data
	 	self.head = self.head.next
	 	self.llsize -= 1
	 	

	 	#If the only Element was removed
	 	if self.isEmpty():
	 		self.tail=None

	 	#Do the memory cleanup
	 	else:
	 		self.head.prev=None

	 	#Return the data removed
	 	return data

	 def removeLast(self):
	 	'''
	 	Remove the Last element from the Linked List, O(1)
	 	'''

	 	#Can't remove from empty list
	 	if self.isEmpty():
	 		raise Exception('Empty List')

	 	'''
	 	Extract the data of the tail Node
	 	And, shif the tail pointer to previous node
	 	'''
	 	data=self.tail.data
	 	self.tail=self.tail.prev
	 	self.llsize -=1

	 	#If the only Item was removed
	 	if self.isEmpty():
	 		self.head=None
	 	#Do a memory cleanup for the removed node
	 	else:
	 		self.tail.next=None

	 	#Return the removed Node data
	 	return data

	 














