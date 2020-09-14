'''
Given an integer array, one element occurs odd number of times and all others have even occurrences. Find the element with odd occurrences.
'''

'''
Method 1: One approach is again to build a hashtable of element occurrence counts and return the element with odd count. Both time and space complexity of this solution is O(N).
'''

'''
Method2: XOR a number with itself odd number of times the result is 0, 
otherwise if we XOR even number of times the result is the number itself
So, if we XOR all the elements in the array, 
the result is the odd occurring element itself. 
Bcz all even occurring elements will be XORed with themselves odd number of times,producing 0. 
And the only odd occurring element will be XORed with itself even number of times, producing its own value.
'''
import functools
def getOdd(arr):
	return functools.reduce(lambda x, y:x^y, arr)

if __name__ == '__main__':
	arr=[1,2,3,1,2,3,1]
	print(getOdd(arr))