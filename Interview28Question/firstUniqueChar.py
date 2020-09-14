# Find the first non-repeated (unique) character in a given string.
#0(N) using hashmap,  Hashtable is generally the key data structure to achieve optimal linear time solutions in questions that involve counting.

import collections

def firstUnique(text):
	counts=collections.defaultdict(int)
	for letter in text:
		counts[letter]+=1

	for letter in text:
		if counts[letter]==1:
			return letter

if __name__ == '__main__':
	text='qwertyubvcxasdfghwedfvbntasrqtokjbv'
	print(firstUnique(text))

