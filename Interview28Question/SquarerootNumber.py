'''
Find the squareroot of a given number rounded down to the nearest integer, without using the sqrt function. 
For example, squareroot of a number between [9, 15] should return 3, and [16, 24] should be 4.
'''

'''
Method 1# The squareroot of a (non-negative) number N always lies between 0 and N/2. 
The straightforward way to solve this problem would be to check every number k between 0 and N/2, 
until the square of k becomes greater than or rqual to N. 
If k^2 becomes equal to N, then we return k. Otherwise, we return k-1 because we’re rounding down. 
complexity of this approach is O(N),because we have to check N/2 numbers in the worst case
'''

def sqrt1(num):
	if num<0:
		raise ValueError

	if num==1:
		return 1

	for k in range(1+(num//2)):
		if k**2 == num:
			return k
		elif k**2 > num:
			return k-1
	return k


'''
Method 2#: An use some sort of binary search to speed it up.
We know that the result is between 0 and N/2, 
so we can first try N/4 to see whether its square is less than, greater than, or equal to N. 
If it’s equal then we simply return that value. 
If it’s less, then we continue our search between N/4 and N/2. 
Otherwise if it’s greater, then we search between 0 and N/4

We want to ensure that we stop at a number k, where k^2<=N but (k+1)^2>N. 
One difference from regular binary search is the condition of the while loop, it’s low+1<high instead of low<high. 
Also we have low=mid instead of low=mid+1, and high=mid instead of high=mid-1. 
The complexity is still the same though, it’s logarithmic O(logN).
'''

def sqrt2(num):
	if num<0:
		raise ValueError

	if num==1:
		return 1

	low=0
	hight 1+(num//2)
	while low+1 < high:
		mid =  low + (high -low )/2
		square = mid**2

		if square == num:
			return square
		elif square < num:
			low = mid
		else:
			high = mid
	return low



if __name__ == '__main__':
	print(sqrt1(999))