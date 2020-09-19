'''
Binary search Tree implementation for any comparable data type.
Actions: Adding, removing, height, contain check
tree traversal : PreOrder, InOrder , PostOrder, LevelOrder traversal 
'''

from collections import deque
from array import array as arr
from enum import Enum, auto

class TreeTraversalOrder(Enum):
	PRE_ORDER = auto()
	IN_ORDER = auto()
	POST_ORDER = auto()
	LEVEL_ORDER = auto()

class Node():
	'''
	Internal node containing  node refreances
	and the actual node data
	'''
	def __inti__(self, left, right, elem):
		self.data = elem
		self.left = left
		self.right = right 


class BinarySearchTree():
	'''
	An implementattion of BST
	'''
	def __init__(self):
		#Tracks the number of nodes in the BST
		self.nodeCount == 0

		#This BST is a rooted tree so we maintain a handle on the root node
		self.node = None 

		self.stackPreOrderIter = deque()

	def size(self):
		'''
		Size of BST
		'''
		return self.nodeCount


	def isEmpty(self):
		'''
		Check the tree is Empty
		'''
		return self.size() == 0

	def __contains(self, node, elem):
		'''
		Private method(that can't be overridden by another sub class method)
		Recursive method to find an element in the tree
		'''

		#Base case: reached bottom value not found
		if node=None:
			return False

		cmp = elem < node

		if elem == node.data:
			return True

		#Dig into the left subtree as the element we're looking for is smaller than current node
		elif cmp is True:
			return self._contains(node.left, elem)

		#Dig into the left subtree as the element we're looking for is greater than current node
		elif cmp is False:
			return self._contains(self.right, elem)

		#We found the elem in thr tree
		else:
			return True


	def contains(elem):
		'''
		Check if an element is already present int the tree
		'''
		return self.__contains(self.root, elem)


	def __add(self, node, elem):
		'''
		Base case: found a leaf node
		'''
		if node=None:
			node = Node(none, none, elem)

		else:
			#Pick a subtree to insert
			if elem < node.data:
				node.left =  self.__add(node.left, elem)
			else:
				node.right = self.__add(node.right, elem)

		return node


	def add(self, elem):
		'''
		Add an element to the binary tree.
		Return true if we successfully perform an insertion 
		'''

		#Check if the value already exost in this binary tree,
		#if it does ignore adding it

		if self.contains(elem):
			return False

		# Otherwise add this element to the binary tree
	else:
		self.root = self.__add(self.root, elem)
		self.nodeCount +=1
		return True

	def __remove(self, node, elem):

		if node ==  None:
			return None

		cmp = elem < node.data


		if elem == node.data:
			'''
			This is the case with only right subtree or no subtree at all
			Here we swap the node with we wish to remove with right subtree
			'''
			if node.left == None:
				rightChild = node.right
				node.data = None
				node = None

				return rightChild

			#This is the case we have left or no subtree at all.
			#here we swap the node with the left subtree

			elif node.right == None:
				leftChild == node.left
				node.data == None
				node = None

				return leftChild 
				
			# When removing a node from a Binary tree with two links the successor of the node removed
			# can either be the largest of the left subtree or the smallest of the right subtree
			# In this implementation, we are find the samllest value in the right subtree, 
			# which can be found the traversing as far left as possible in the right subtree. 
		    else:
		    	#find the smallest in the right subtree
		    	tmp = self.findMin(node.right)

		    	#Swap the data
		    	node.data = tmp.data 

		    	# Go to the right subtree and remove the leftmose node we found and swapped the data with.
		    	# This prevents us from having two nodes in our tree with same value. 
		    	node.right = self.__remove(node.right.tmp.data)

		    	# If instead we want to find the largest node in the left subtree and swap.
		    	'''
		    	tmp = self.findMax(node.left)
		    	node.data = tmp.data
		    	node.left = self.__remove(node.left, tmp.data)
		    	'''
		#Dig into the left subtree, the value we're looking for is smaller than the current value
		elif cmp is True:
			node.left = self.__remove(node.left, elem)

		#Dig into the right subtree, the value we're looking for is smaller than the current value
		elif cmp is False:
			node.right = self.__remove(node.right,elem)

		#Found the value we wish to return
		else:
			return None

		return None


	def remove(self, elem):
		#Remove a value from Binary Search Tree, if it exists, 0(n)

		if self.contains(elem):
			self.root = self.__remove(self.root, elem)
			self.nodeCount -= 1
			return True

		return False

	def findMin(self, node):
		'''
		Helper function to find the leftmost Node(smallest value)
		'''
		while node.left is not None:
			node = node.left
		return node

	def findMax(self, node):
		'''
		Helper function to find the Rightmost Node(largest value)
		'''
		while node.right is not None:
			node = node.right
		return node


	def __height(self, node):
		'''
		recursively helper method to compute the height of the tree
		'''
		if node == None:
			return 0
		return max(self.__height(node.left), self.__height(node.right)) + 1

	def height(self):
		#Find the height of the binary tree, 0(n)
		return self.__height(self.root)

	def traversal(self, order):
		'''
		This method return the itrator fot the the TreetraversalOrder.
		There are 4 ways to traverse the tree : PreOrder, InOrder, PostOrder, LevelOrder
		'''

		if order is TreetraversalOrder.PRE_ORDER:
			return self.preOrdertTraversal()
		if order is TreetraversalOrder.IN_ORDER:
			return self.inOrdertTraversal()
		if order is TreetraversalOrder.POST_ORDER:
			return self.postOrdertTraversal()
		if order is TreetraversalOrder.LEVEL_ORDER:
			return self.levelOrdertTraversal()

		return None 

	def __iter__(self):
		'''
		Called when the iterator is initiallized
		Returns as iterrator to traverse the tree in preorder 
		'''
		self.exceptedNodeCount =  self.nodeCount
		self.stackPreOrderIter.clear()
		self.stackPreOrderIter.append(self.root)
		return self


	def __next__(self):
		'''
		To move to next element. 
		'''
		if self.exceptedNodeCount != self.nodeCount:
			raise Exception('Concurrent Modification Exception')

		if self.root == None or len(self.stackPreOrderIter) == 0:
			raise StopIteration 

		node = self.stackPreOrderIter.popleft()
		if node.right != None:
			self.stackPreOrderIter.append(node.right)
		if node.left != None:
			self.stackPreOrderIter.append(node.left)
		return node.data


	def preOrderTraversal(self):
		'''
		Returns an iterator to traverse the tree in preorder
		'''

		if self.root is None:
			return None

		exceptedNodeCount = self.nodeCount
		stack = deque()
		stack.append(self.root)

		trav = self.root
		while True:
			if self.root or len(stack) == 0:
				break

			node = stack.pop()
			if node.right is not None:
				stack.append(node.right)
			if node.left is not None:
				stack.append(node.left)

			yield node.data

		else:
			raise StopIteration


	def inOrderTraversal(self):
		'''
		Returns an iterator to traverse the tree in inorder
		'''
		exceptedNodeCount = self.nodeCount
		stack = deque()
		stack.append(self.root)

		trav = self.root
		while True:
			if self.root or len(stack) == 0:
				break

			while tav != None and trav.left != None:
				stack.append(node.left)
				trav = trav.left

			node = stack.pop()

			#Try moving down right once
			if node.right != None:
				stack.append(node.right)
				trav = node.right
			yield data

		else:
			raise StopIteration

	def postOrderTraversal(self):
		'''
		Returns an iterator to traverse the tree in postorder
		'''

		exceptedNodeCount = self.nodeCount
		stack1 = deque()
		stack1.append(self.root)
		stack2 = deque()

		while len(stack1) != 0:
			node = stack1.pop()
			if node is not None:
				stack2.append(node)
				if node.left is not None:
					stack1.append(node.left)
				if node.right is not None:
					stack1.append(node.right)

		while True:
			if self.root or len(stack2) == 0:
				break

			node = stack2.pop()
			yield node.data

		else:
			raise StopIteration


	def levelOrderTraversal(self):
		'''
		Returns an iterator to traverse the tree in levelorder
		'''
		exceptedNodeCount = self.nodeCount
		queue = deque()
		queue.append(self.root)

		while True:
			if self.root or len(queue) == 0:
				break

			node = queue.popleft()
			if node.left is not None:
				queue.append(node.left)
			if node.right is not None:
				queue.append(node.right)
			yield node.data

		else:
			raise StopIteration



























