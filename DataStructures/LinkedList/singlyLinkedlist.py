class Node:
	def __init__(self, data):
		self.data = data	#Contains data
		self.next = None	#Initialize next

class LinkedList:
	def __init__(self):
		self.head = None	#Initialize head

	#Insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)	#create a new node
		new_node.next=self.head		# Add the new Node 
		self.head = new_node	# change head to new Node

	#Append at the end	
	def append(self, new_data):
		new_node=Node(new_data)

		# If list is empty, add to the beginnning 
		if self.head is None:
			self.head=new_node
			return

		trav=self.head
		
		#traverse to the end of the list
		while trav.next:
			trav=trav.next

		#Add the new node to the end 
		trav.next = new_node

	def InsertAfer(self, prev_node, new_data):
		trav=self.head
		while trav and trav.data != prev_node:
				trav=trav.next

		if trav is None:
			print("No such node")
			return
		else:
			new_node=Node(new_data)	
			new_node.next = trav.next
			trav.next = new_node
			return
		return

	def deleteNode(self, key):
		trav = self.head

		#delete at beginning 
		if trav and trav.data==key:
			self.head = trav.next
			trav=None
			return

		# delete after 1st node
		prev= None
		while trav and trav.data != key:
			prev = trav
			trav=trav.next

		if trav is None:
			print("No such Node")
			return
		else:
			prev.next = trav.next
			trav=None
		return

	def deleteAtIndex(self, pos):
		trav=self.head
		if pos==0:
			self.head = trav.next
			trav=None
			return

		count=0
		prev=None
		while trav and count != pos:
			prev=trav
			trav =trav.next
			count+=1

		if trav is None:
			print("Out of Bound Position:", pos)
			return
		else:
			prev.next = trav.next
			trav=None
		return

	def len_iterative(self):
		count=0
		trav=self.head

		while trav:
			count+=1
			trav =trav.next
		return count

	def len_recursive(self, node):
		if node is None:
			return 0
		return (1 + self.len_recursive(node.next))



		#swap the keys 
	def swap_nodes(self, key1, key2):
		if key1==key2:
			return

		trav1=trav2=self.head
		prev1=prev2=None

		#Seek to the keys
		while trav1 and trav1.data != key1:
			prev1 = trav1
			trav1= trav1.next

		while trav2 and trav2.data != key2:
			prev2 = trav2
			trav2  = trav2.next

		#Keys not found  
		if not trav1 or not trav2:
			return

		if prev1:
			prev1.next=trav2
		else: 
			self.head=trav2

		if prev2:
			prev2.next=trav1
		else:
			self.head=trav1 

		trav1.next, trav2.next = trav2.next, trav1.next
		return

	# Reverse the list
	def reverse_iter(self):
		trav=self.head
		prev=None
		while trav:
			next =  trav.next
			trav.next = prev
			prev = trav
			trav = next

		self.head=prev
			

	def reverse_recursive(self):
		def _reverse_recursive(cur, prev):
			if not cur:
				return prev
			next =  cur.next
			cur.next = prev
			prev = cur
			cur = next
			return _reverse_recursive(cur, prev)

		self.head = _reverse_recursive(cur=self.head, prev=None )



	# print the LinkedLists
	def printList(self):
		trav = self.head  # Set traversal pointer to head
		while trav:
			print(trav.data,end="-->")
			trav = trav.next
		print("NULL")



if __name__=='__main__':
	llist = LinkedList()  # create a LinkedList object

	llist.push('C')
	llist.push('B')
	llist.push('A')
	llist.append('D')
	#llist.InsertAfer('B', 'E')
	llist.printList()
	#llist.InsertAfer('F', 'E')
	#llist.printList()
	#llist.deleteNode('E')
	#llist.deleteAtIndex(0)
	llist.printList()
	print("Length Iterative: ", llist.len_iterative() )
	print("Length Recursive: ", llist.len_recursive(llist.head) )
	#llist.swap_nodes('B', 'D')
	llist.reverse_iter()
	llist.printList()
	llist.reverse_recursive()
	llist.printList()






