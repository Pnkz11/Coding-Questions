'''
Given a binary tree of integers, print it in reverse level order. 
The output will contain space between the numbers in the same level, 
and new line between different levels.
Input:  1
	   / \
	  2   3
	 /   / \
	4   5   6

Output:
4 5 6
2 3
1
'''

'''
Breadth first search (BFS) from the root of the tree and push each node to a queue.
Printing will be take place a separate loop after completing breadth first search.
count the number of nodes in each level and push them to a stack
After BFS, we have the following two data structures:
Queue of nodes: [1, 2, 3, 4, 5, 6]
Stack of node counts at each level: [3, 2, 1], this has 1st as deepest level and at last we have root
'''

def reverseLevelOrderPrint(tree):
	if not tree:
		return
	nodes=[tree] #queue
	levelCount=collections.deque([1])    #Stack
	currentCount, nextCount = 1, 0
	i=0

	while i<len(nodes):
		currentNode=node[i]
		currentNode-=1
		if currentNode.left:
			nodes.append(currentNode.left)
			nextCount+=1
		if currentNode.right:
			nodes.append(currentNode.right)
			nextCount+=1
		if currentCount==0:
			#fininshed the level
			if nextCount==0:
				#no more nodes at next level
				break
			#continue with next level
			levelCount.appendleft(nextCount)
			currentCount, nextCount = nextCount, currentCount
		i+=1
	printIndex=len(nodes)
	for count in levelCount:
		output = nodes[printIndex-count:printIndex]
		print(' '.join(map(str, output)), '\n')
		printIndex-=count


