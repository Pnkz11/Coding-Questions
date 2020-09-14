def precomputeSum(matrix):
	topRow, bottomRow = (0, len(matrix) - 1)
	leftCol, rightCol = (0, len(matrix[0]) -1)
	sums=[[0] * (rightCol - leftCol+1) for i in range(bottomRow - topRow +1)]
	print('Sums: {}, [0]: {}', sums, [0] )
	sums[topRow][leftCol]=matrix[topRow][leftCol]

	for col in range(leftCol+1, rightCol+1):
		sums[topRow][col] = sums[topRow][col-1] + matrix[topRow][col]
	for row in range(topRow +1, bottomRow+1):
		sums[row][leftCol] = sums[row-1][leftCol] + matrix[row][leftCol]

	for col in range(leftCol+1, rightCol+1):
		columnSum=matrix[topRow][col]
		for row in range(topRow+1, bottomRow+1):
			sums[row][col] =sums[row][col-1] + matrix[row][col] + columnSum
			columnSum+=matrix[row][col]

	return sums

def matrixRegionSum2(matrix, A, D, sums):
	# A, D are lists with matrix coordinate{row,column} e.g A=[2,3]
	if len(matrix)==0:
		return 

	if A[0]==0 or A[1]==0:
		OA=0
	else:
		OA=sums[A[0]-1][A[1]-1]

	if A[1]==0:
		OC=0
	else:
		OC=sums[D[0]][A[0]-1]

	if A[0]==0:
		OB=0
	else:
		OB=sums[A[0]-1][D[1]]

	OD=sums[D[0]][D[1]]
	print(OA, OB, OC, OD)

	return OD+OA-OB-OC


#bruteforce
def matrixRegionSum1(matrix, A, D):
    if len(matrix)==0:
        return
    totalSum=0
    for i in range(A[0], D[0]+1):
        for j in range(A[1], D[1]+1):
            totalSum+=matrix[i][j]
    return totalSum


if __name__ == '__main__':
	matrix = [[1,  2,  3,  4,5],
			  [6,  7,  8,  9,10],
			  [11, 12, 13, 14,15],
			  [16, 17, 18, 19,20],
			  [21, 22, 23, 24,25]]
	A=[1,1]
	D=[2,2]
	sums=precomputeSum(matrix)
	print (sums)
	result=matrixRegionSum2(matrix, A, D, sums)
	#result=matrixRegionSum1(matrix, A, D)
	print('Result:',result)

