 
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

	 def __remove__(self, node):
	 	'''
	 	Remove an arbitrary node from the Linked List, O(1)
	 	'''
	 	
	 	#If the node to remove is either at the head or tail 
	 	if node.prev == None:
	 		return self.removeFirst()

	 	if node.next == None:
	 		return self.removeLast()

	 	#Make the pointer of the adjacent node skip over 'node'
	 	node.next.prev = node.prev
	 	node.prev.next = node.next

	 	#Temporarily store the data we want to return
	 	data = node.data

	 	#Memory cleanup
	 	node.data = None 
	 	node.next = None
	 	node.prev = None
	 	node = None

	 	self.llsize -=1

	 	#Return the data in the node that was removed
	 	return data

	def removeAt(self, index):
		'''
		Remove node at a particular index, O(n)
		'''

		#Make sure index provided is a valid index
		if index < 0 or index>=self.llsize:
			raise valueError('Wrong Index')

		#Search for Node at Index from front
		if index < self.llsize//2:
			i = 0
			trav = self.head
			while i != index:
				i += 1
				trav = trav.next

		#Search from the tail/back of the Linked List
		else:
			i = self.llsize - 1
			trav = self.tail
			while i != index:
				i -= 1
				trav = trav.prev

		return self.__remove__(trav)

	def remove(self, obj):
		'''
		Remove a particular value in the Linkedlist, O(n)
		'''
		trav = self.head

		#Support search for Null
		if obj is None:
			trav = self.head
			while trav is not None:
				if trav.data is None:
					self.__remove__(trav)
					return True

				trav=trav.next

		#Search for not null Object
		else:
			trav = self.head

			while trav is not None:
				if trav.data == obj:
					self.__remove__(trav)
					return True
				
				trav = trav.next

		return False

	def indexOf(self, obj):
		'''
		Find the index of a particular value in the Linked List, 0(n)
		'''
		index = 0 
		trav = self.head

		#Support search for null
		if obj is None:
			while trav is not None:
				if trav.dat is None:
					return index
				trav = trav.next
				index +=1

		#Search for the non null object
	else:
		while trav in not None:
			if obj == trav.data:
				return index
			
			trav = trav.data
			
			index +=1

		return -1

	def contain(self, obj):
		'''
		check if the list contains a given object
		'''
		return self.indexOf(obj) != -1 

	def __iter__(self):
		'''
		called when iteration is initiallized
		'''
		self.travIter = self.head
		return self

	def __next__(self):
		'''
		To move to next element
		'''
		#Stop Iteration when limit is reached
		if self.travIter is None:
			raise StopIteration 

		#Stop current travIter.data
		data = self.travIter.data
		self.travIter = self.travIter.next

		#Else increment and return the data
		return data

	def __repr__(self):
		sb = ""
		sb = + '['
		trav = self.head
		while trav in not None:
			sb = sb + str(trav.dat)
			if trav.next is not None:
				sb = sb + ','

			trav = trav.next

		sb = sb + ' ]'

		return str(sb)
	
















	 














