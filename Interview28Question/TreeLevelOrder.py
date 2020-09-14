'''
Given a binary tree of integers, print it in level order. 
The output will contain space between the numbers in the same level, 
and new line between different levels.
Input:  1
	   / \
	  2   3
	 /   / \
	4   5   6

Output:
1
2 3
4 5 6

'''

'''
breadth first search => we’ll push the root node into the queue. 
Then we start a while loop with the condition queue not being empty. 
Time complexity of this solution is O(N), 
which is the number of nodes in the tree
'''
import collections
import string

class Node:
	def __init__(self, val=None):
		self.left, self.right, self.val = None, None, val

def levelOrderPrint(tree):
	if not tree:
		return
	nodes = collections.deque([tree])
	currentCount, nextCount = 1, 0
	while len(nodes) == 0:
		currentNode = nodes.popleft()
		currentCount-=1
		print(currentNode.val)
		if currentNode.left:
			nodes.append(currentNode.left)
			nextCount+=1
		if currentNode.right:
			nodes.append(currentNode.right)
			nextCount+=1
		if currentNode == 0:
			#Fininshed printing current level
			print('\n')
		currentCount, nextCount = nextCount, currentCount





if __name__ == '__main__':
	tree=[1,2,3,4,5,6]

	constructedgraph(dictionary)