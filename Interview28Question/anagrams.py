#Given two strings, check if they’re anagrams or not. Two strings are anagrams if they are written using the same exact letters, ignoring space, punctuation and capitalization. 


#method 1: sort both strings and check whether they’re the same or not. 
#The complexity is O(NlogN) where N is the number of characters in the string

from string import *

def isAnagrams1(str1, str2):
	return sorted(getLetters(str1)) == sorted(getLetters(str2))

def getLetters(text):
	return [char.lower() for char in text if char in ascii_letters]


#Method2: Since the problem involves counting, hashtable would be a suitable data structure
#The complexity of this solution is O(N), which is optimal.

import collections

def isAnagrams2(str1, str2):
	str1, str2 = getLetters(str1), getLetters(str2)

	if len(str1) != len(str2):
		return False

	counts = collections.defaultdict(int)

	for letter in str1:
		counts[letter]+=1

	for letter in str2:
		counts[letter]-=1
		if counts[letter] < 0:
			return False

	return True

if __name__ == '__main__':
	str1= 'qwer asdf zxcv'
	str2= 'asdf qter cxzv'
	print(isAnagrams2(str1, str2))