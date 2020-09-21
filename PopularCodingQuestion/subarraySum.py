'''
Find subarray with given sum
'''

def subArraySum(arr, n , Sum):
	#Create an empty map
	Map = {}

	#Maintains sum of elements so far
	curr_sum = 0

	for i in range(0, n):
		#Add current element to curr_sum
		curr_sum += arr[i]

		if curr_sum == Sum:
			print("Sum found in Indexes 0 to ",i)
			return

		if (curr_sum - Sum) in Map:
			print("Sum between indexes", Map[curr_sum - Sum] +1 , "to " ,i)
			return
		Map[curr_sum] = i
	print(Map)
	return
	print("No such subArray")


if __name__=='__main__':
	array = [3,5,12,98, 45,2,9]
	subArraySum(array, len(array), 11)



