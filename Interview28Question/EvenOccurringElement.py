#Given an integer array, one element occurs even number of times and all others have odd occurrences. 
#Find the element with even occurrences.

#Hashtable for counting.Scan the array and count the occurrences
# perform a second pass from the hashtable and return the element with even count.
# complexity O(N)

import collections
def getEven(arr):
	counts=collections.defaultdict(int)
	for num in arr:
		counts[num]+=1

	for num, count in counts.items():
		if count%2==0:
			return num

#Method2 : Using XOR method, O(N), if we XOR a number with itself odd number of times we get 0, 
# otherwise if we XOR even number of times then we get the number itself. 
from functools import reduce
def getEven2(arr):
	return reduce(lambda x,y: x^y, arr+list(set(arr)))
if __name__ == '__main__':
	arr=[2, 3, 4, 1, 3]
	print(getEven2(arr))