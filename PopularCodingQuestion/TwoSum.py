'''
Method 1: BruteForce, O(n^2)
Method 2: Compliment, O(n)
'''

class TwoSum():
	def __int__(self):
		pass

	def twoSumBF(self, nums, target):
		for i in range(len(nums)):
			for j in range(i+1, len(nums)):
				sum = nums[j] + nums[i]
				if sum == target:
					return [i,j]
		return -1

	def twoSumComplement(self, nums, target):
		complimentMap = dict()

		for i in range(len(nums)):
			compliment = target - nums[i]

			if nums[i] in complimentMap:
				return [complimentMap[nums[i]], i]
			else:
				complimentMap[compliment] = i

		return -1

if __name__=='__main__':
	s = TwoSum()
	arr = [1,2,3,4,5,6,7,8,9,10,11]
	print(s.twoSumComplement(arr, 11))




