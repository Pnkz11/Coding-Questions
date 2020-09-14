# Given an array: [a_1, a_2, …, a_N, b_1, b_2, …, b_N, c_1, c_2, …, c_N ]
# convert it to: [a_1, b_1, c_1, a_2, b_2, c_2, …, a_N, b_N, c_N]


def getIndex(currentIndex, N):
	return int((currentIndex%3)*N + (currentIndex//3))

# function with Extra space i.e create new array
def convertArray_extraspace(arr):
	N=len(arr)/3
	return [arr[getIndex(i, N)] for i in range(len(arr))]

# no extra space is allowed i.e need to change same array . Time complexity O(N^1.3)
def convertArray(arr):
	N=len(arr)/3
	for currentIndex in range(len(arr)):
		swapIndex=getIndex(currentIndex, N)

		while swapIndex<currentIndex:
			swapIndex=getIndex(swapIndex, N)
		arr[currentIndex], arr[swapIndex] = arr[swapIndex], arr[currentIndex]

# to plot complexity of the function convertArray
def complexityAnalysis():
	x=range(3, 1000, 3)
	y=[convertArray(range(num)) for num in x]
	pylab.plot(x, sorted(y), label='convertArray')
	pylab.plot(x, map(lambda num: num*1.2, x), label='x^1.2')
	pylab.plot(x, map(lambda num: num*1.3, x), label='x^1.3')
	pylab.legend(loc='upper left')
	pylab.title("complexity of convertArray")
	pylab.xlabel('array length')
	pylab.ylabel('number of getIndex calls')
	pylab.show()

if __name__ == '__main__':
	arr=[1,2,3,4,5,11, 12, 13, 14, 15, 21, 22, 23, 24, 25]
	convertArray(arr)
	print(arr)
	complexityAnalysis()
