'''
Given a text file and a word, find the positions that the word occurs in the file. 
We’ll be asked to find the positions of many words in the same file.
'''

'''
build a data structure that stores the positions of all the words in the text file. 
This is known as inverted index in Information Retrieval.==> Hashtable -> words: [positions] 
Time and space complexity O(N)
'''
import re, collections

def getWords(text):
	return re.sub(r'[^a-z0-9]', ' ', text.lower()).split()

def createIndex1(text):
	index=collection.defaultdict(list)
	words=getWords(text)
	for pos, word in enumerate(words):
		index[word].append(pos)
	return index

def queryIndex1(index, word):
	if word in index:
		return index[word]
	else:
		return []

'''
Using hashtable as the inverted index is pretty efficient. 
method 2: But we can do better by using a more space efficient data structure for text, 
namely a trie, also known as prefix tree.
Trie is a tree which is very efficient in text storage and search. 
It saves space by letting the words that have the same prefixes to share data. 
And most languages contain many words that share the same prefix.
'''

#define Trie

class Node:
	def __init__(self, letter):
		self.letter=letter
		self.isTerminal = False
		self.children={}
		self.positions=[]

class Trie:
	def __init__(self):
		self.root=Node('')

	def __contains__(self, word):
		current=self.root
		for letter in word:
			if letter not in current.children:
				return False
			current=current.children
		return current.isTerminal

	def __getitem__(self, word):
		current=self.root
		for letter in word:
			if letter not in current.children:
				current.children[letter]=Node(letter)
			current=current.children[letter]
		current.isTerminal=True
		print(current.positions)
		return current.positions

	def __str__(self):
		self.output([self.root])
		return ' '

	def output(self, currentPath, indent=''):
		#Depth Forst Search
		currentNode=currentPath[-1]
		if currentNode.isTerminal:
			word=' '.join([node.letter for node in currentPath])
			print(indent+word+ ' '+ str(currentNode.positions))
			indent+='	'

		for letter, node in sorted(currentNode.children.item()):
			self.output(currentPath[:] + [node] , indent)


#createIndex and queryIndex functions 
def createIndex2(text):
	trie=Trie()
	words=getWords(text)
	for pos, word in enumerate(words):
		trie[word].append(pos)
	return trie

def queryIndex2(index, word):
	if word in index:
		return index[word]
	else:
		return []

if __name__ == '__main__':
	text='us use uses used user users using useful username user utah'
	index=createIndex2(text)
	queryIndex2(index, 'user')




		