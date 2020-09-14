##Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

if __name__=='__main__':
	t=int(input())
	while t>0:
		n_k=[int(x) for x in input().strip().split()]
		n=n_k[0]
		k=n_k[1]

		list=[int(x) for x in input().strip().split()]
		start,last,cursum,flag=0,0,0,False

		for i in range(n):
			cursum += list[i]
			print(cursum)
			if cursum >= k:
				last=i
				while(k< cursum and start < last):
					cursum -= list[start]
					start = start + 1
				if cursum == k:
					print(str(start+1) + "  " + str(last+1))
					flag=True
					break
		if flag == False:
			print(-1)
		t =t-1
