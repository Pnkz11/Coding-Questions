'''
Given a sorted list of words, find the longest compound word in the list that is constructed by concatenating the words in the list. 
For example, if the input list is: [‘cat’, ‘cats’, ‘catsdogcats’, ‘catxdogcatsrat’, ‘dog’, ‘dogcatsdog’, ‘hippopotamuses’, ‘rat’, ‘ratcat’, ‘ratcatdog’, ‘ratcatdogcat’]. 
Then the longest compound word is ‘ratcatdogcat’ with 12 letters. 
Note that the longest individual words are ‘catxdogcatsrat’ and ‘hippopotamuses’ with 14 letters, but they’re not fully constructed by other words. 
Former one has an extra ‘x’ letter, and latter is an individual word by itself not a compound word.
'''

'''
We will use the trie data structure, also known as a prefix tree. 
Tries are space and time efficient structures for text storage and search.  
They let words to share prefixes, and prefixes are exactly what we’ll be dealing with in this question.
The complexity of this algorithm is O(kN) 
where N is the number of words in the input list, and k the maximum number of words in a compound word. 
'''

class Node:
	def __init__(self, letter=None, isTerminal=False):
		self.letter=letter
		self.children={}
		self.isTerminal=isTerminal

class Trie:
	def __init__(self):
		self.root= Node(' ')

	def __repr__(self):
		self.output([self.root])

	def output(self, currentPath, indent=' '):
		#Depth first search
		currentNode=currentPath[-1]
		if currentNode.isTerminal:
			word = ' '.join([node.letter for node in currentPath])
			print(indent + word)
			indent +='	'

		for letter, node  in sorted(currentNode.children ):
			self.output(currentPath[:]+[node], indent)

		
	def insert(self, word):
		current = self.root
		for letter in word:
			if letter not in current.children:
				current.children[letter]=Node(letter)
			current = current.children[letter]
		current.isTerminal=True

		def __contains__(self, word):
			current = self.root
			for letter in word:
				if letter not in current.children:
					return False
				current=current.children[letter]
			current.isTerminal=True

	def getAllPrefixOfWord(self, word):
		prefix=''
		prefixes=[]
		current=self.root
		for letter in word:
			if letter not in current.children:
				return prefixes
			current=current.children[letter]
			prefix+=letter
			if current.isTerminal:
				prefixes.append(prefix)
		return prefixes

import collections

def longestWord(words):
	#Add words to the trie, and pairs to the queue
	trie=Trie()
	queue=collections.deque()
    

	for word in words:
		trie.insert(word)

	#breakpoint()
	for word in words:
		prefixes = trie.getAllPrefixOfWord(word)
		for prefix in prefixes:
			queue.append( (word, word[len(prefix):]))
		trie.insert(word)

	#Process the queue
	longestWord=''
	maxLength=0
	while queue:
		word, suffix = queue.popleft()
		if suffix in trie and len(word) > maxLength:
			longestWord = word
			maxLength = len(word)
		else: 
			prefixes = trie.getAllPrefixOfWord(suffix)
			for prefix in prefixes:
				queue.append((word, suffix[len(prefix)]))
	return longestWord


if __name__ == '__main__':
	words = ['cat', 'cats', 'catsdogcats', 'catxdogcatsrat', 'dog', 'dogcatsdog', 'hippopotamuses', 'rat', 'ratcat', 'ratcatdog', 'ratcatdogcat']
	print(longestWord(words))