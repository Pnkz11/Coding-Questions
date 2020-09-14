#Using bruteforce complexity Space O(N) , Time O(NlogN)
def findMissingNum1(arr1, arr2):
	arr1.sort()
	arr2.sort()

	for num1. num2 in zip(arr1, arr2):
		if num1!=num2:
			return num1
	return arr1[-1]

#Using hashtable method complexity Space O(N) , Time O(N)
def findMisssingNum2(arr1,arr2):
	d =collections.defaultdict(int)

	for num in arr2:
		d[num]+=1

	for num in arr1:
		if d[num]==0:
			return num
		else:
			d[num]-=1

#Using XOR method complexity Space(1) , Time O(N)
def findMissingNum3(arr1,arr2):
	result=0
	for num in arr1 + arr2:
		print(arr1+arr2)
		result^=num
	return result


#Using XOR method using reduce complexity Space(1) , Time O(N)
from functools import reduce

def dup_findMissingNum3(arr1,arr2):
	return reduce(lambda x,y:x^y, arr1+arr2)
	


if __name__ == '__main__':
	arr1=[1,2,5,6]
	arr2=[5,6,1]
	result=dup_findMissingNum3(arr1,arr2)
	print(result)


	