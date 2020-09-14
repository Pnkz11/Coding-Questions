'''
Given a source word, target word and an English dictionary, 
transform the source word to target by changing/adding/removing 1 character at a time, 
while all intermediate words being valid English words. 
Return the transformation chain which has the smallest number of intermediate words.
'''

'''
Solution using breadth first search, 
Breadth first search gives the shortest path between a start node and a goal node in an unweighted graph.
To generate graph where each edge corresponds to a valid transformation between words.
'''
import collections
import string

def constructedgraph(dictionary):
	graph=collections.defaultdict(list)
	letters = string.ascii_lowercase

	for word in dictionary:
		for i in range(len(word)):
			#remove 1 charecter
			remove= word[:i] + word[i+1:]
			#breakpoint()
			if remove in dictionary:
				graph[word].append(remove)
			#change 1 charecter 
			for char in letters:
				change= word[:i] + char + word[i+1:]
				if change in dictionary and change != word:
					graph[word].append(change)

		#add 1 character 
		for i in range(len(word)+1):
			for char in letters:
				add=word[:i]+char+word[i:]
			if add in dictionary:
				graph[word].append(add)

	return graph

'''
given two words we can initiate a breadth first search from the start node and 
once we reach the goal node we will have the shortest chain of transformations between two words 
'''
def transformWord(graph, start, goal):
	paths=collections.deque([[start]])
	extended = set()
	#BFS
	while len(paths) !=0:
		currentPath = paths.popleft()
		currentWord = currentPath[-1]
		breakpoint()
		if currentWord == goal:
			return currentPath
		elif currentWord in extended:
			#already extended the word
			continue
		extended.add(currentWord)
		transforms = graph[currentWord]

		for word in transforms:
			if word not in currentPath:
				#avpid loops
				paths.append(currentPath[:]+ [word])
	#no transformation
	return []



if __name__ == '__main__':
	dictionary=['cat','bat', 'bet', 'bed', 'at', 'ad', 'ed']
	graph=collections.defaultdict(list)
	graph = constructedgraph(dictionary)
	print(transformWord(graph, 'cat', 'bed'))