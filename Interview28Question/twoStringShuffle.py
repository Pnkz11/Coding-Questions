#Find if String3 is a valid shuffle for Sring1 and String2

#Using recursion complexity exponential

def isShuffle(str1, str2, str3):
	if len(str1) + len(str2) != len(str3):
		return False

	if not str1 or not str2 or not str3:
		if str1 + str2 == str3:
			return True
		else:
			return False

	if str1[0] != str3[0] and str2[0] != str3[0]:
		return False

	if str1[0] == str3[0] and isShuffle(str[1:], str2, str3[1:]):
		return True
	if str2[0] == str3[0] and isShuffle(str1, str2[1:], str3[1:]):
		return True
	
	return False

#Using DP and caching, O 

def isShuffle_DP(str1, str2, str3, cache=set()):
	if (str1, str2) in cache:
		return False

	if len(str1) + len(str2) != len(str3):
		return False

	if not str1 or not str2 or not str3:
		if str1 + str2 == str3:
			return True
		else:
			return False

	if str1[0] != str3[0] and str2[0] != str3[0]:
		return False
	

	if str1[0] == str3[0] and isShuffle_DP(str1[1:], str2, str3[1:], cache):
		return True
	if str2[0] == str3[0] and isShuffle_DP(str1, str2[1:], str3[1:], cache):
		return True

	cache.add((str1, str2))
	print(cache)
	return False

if __name__ == '__main__':
	str1='abcd'
	str2='defg'
	str3='debfcsdg'
	print(isShuffle_DP(str1,str2,str3))