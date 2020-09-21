'''
Interpolation Seach -> codition : sorted Array and uniformally distributed values.
e.g 1, 3, 5 7, 9, 11  ==> This is a sorted Array with gap/difference of 2
'''

class InterpolationSearch():
	'''
	A fast alternative to a binary Seach when the elemwnts are uniformally distributed.
	This algorithms run in time complexity of ~O(log(log(n)))
	'''
	def __init__(self):
		pass

	def interpolationSearch(self, nums, val):
		'''
		@param nums - an ordered list containing uniformly distributed values.
    	@param val - the value we're looking for in 'nums'
    	'''

		lo = 0
		mid = 0
		hi = len(nums) -1

		while nums[lo] <= val and nums[hi] >= val:
			mid = lo + ((val - nums[lo]) * (hi - lo)) // (nums[hi] - nums[lo])
			if nums[mid] < val:
				lo = mid + 1
			elif nums[mid] > val:
				hi = mid - 1
			else:
				return mid

		#if nums[lo] == val:
		#	return lo
		return -1

if __name__ == '__main__':
	"""
	Example usage
	"""
	s = InterpolationSearch()
    
	values = [10, 20, 25, 35, 50, 70, 85, 100, 110, 120, 125]

	# Since 25 exists in the values array the interpolation search
	# returns that it has found 25 at the index 2
	print(s.interpolationSearch(values, 10))

	# 111 does not exist so we get -1 as an index value
	print(s.interpolationSearch(values, 111))



