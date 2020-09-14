def count_set_dp(arr, total):
	mem={}
	return dp(arr, total, len(arr)-1, mem)

def dp(arr, total, i , mem):
	key = str(total) + ' ' + str(i)
	print("Key:", key)

	if key in mem:
		print("mem[key]: ",mem[key])
		return mem[key]

	if total == 0:
		return 1

	elif total < 0:
		return 0

	elif i < 0:
		return 0

	elif total < arr[i]:
		to_return = dp(arr, total, i-1, mem)

	else:
		to_return = (dp(arr, total-arr[i], i-1, mem) + dp(arr, total, i-1, mem))

	mem[key] = to_return
	return to_return

if __name__=="__main__":
	arr = [1, 2, 3, 7, 5 , 14]
	total = 12
	result=count_set_dp(arr, total)
	print("Result:", result)