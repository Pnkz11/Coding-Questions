'''
Given a number, find the next higher number using only the digits in the given number. 
For example if the given number is 1234, next higher number with same digits is 1243.
'''

'''
We scan the digits of the given number starting from the tenths digit (which is 4 in our case) going towards left.
At each iteration we check the right digit of the current digit we’re at, 
and if the value of right is greater than current we stop, otherwise we continue to left
complexity O(logN)
'''

def nextHighest(num):
	strNum=str(num)
	length=len(strNum)

	for i in range(length-2, -1, -1):
		current=strNum[i]
		right=strNum[i+1]

		if current<right:
			temp=sorted(strNum[i:])
			breakpoint()
			next=temp[temp.index(current)+1]
			temp.remove(next)
			temp=''.join(temp)
			return int(strNum[:i]+next+temp)

		return num

if __name__ == '__main__':
	num=12345
	nextHighest(num)


