#permutation function call for get the perms 0(N) and loop for creating permutation of words O(N!)
# Hence, time complaxity 0(N * N!)


def permutations(word):
	if len(word) <=1:
		return(word)

	#get all permutaions of length N-1
	perms=permutations(word[1:])
	char=word[0]
	result=[]
	#iterate  of all the permutations of length N-1
	for perm in perms:
		#insert the charecter into every possible location
		for i in range(len(perm)+ 1):
			result.append(perm[:i] + char + perm[i:])
			breakpoint()
	return result

if __name__ == '__main__':
	word='ABCD'
	print(permutations(word))
