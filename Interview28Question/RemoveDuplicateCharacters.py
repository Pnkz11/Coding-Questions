'''
Remove duplicate characters in a given string keeping only the first occurrences. 
For example, if the input is ‘tree traversal’ the output will be ‘tre avsl’.
'''

'''
Set data structure perfectly suits.
It stores keys and provides constant time search for key existence. 
loop over the characters of the string, 
And at each iteration, check whether we have seen the current character before by searching the set.
Time complexity 0(N)
'''

def removeDuplicates(string):
	result=[]
	seen=set()
	for char in string:
		if char not in seen:
			seen.add(char)
			result.append(char)
	return ''.join(result)

#remove/ignore spaces
def removeDuplicates1(string,ignoreSpaces=True):
	result=[]
	seen=set()
	for char in string:
		if char not in seen:
			seen.add(char)
			result.append(char)
		elif char==' ' and ignoreSpaces:
			result.append(char)	
	return ''.join(result)


if __name__ == '__main__':
	string='tree traversal'
	print(removeDuplicates(string))



