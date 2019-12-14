A = [[1,2,3],
	 [4,5,6],
	 [7,8,9],
	 [10,11,12]]

B = [[1,0,0,1],
	 [0,1,0,1],
	 [0,0,1,0]]

C = []

# a = MxN
# b = NxT

m = len(A)
n = len(A[0])
t = len(B[0])

if len(B) != n:
	print("These matrices cannot be multiplied")
else:
	for i in range(m):
		row = []
		for j in range(t):
			sum = 0
			for k in range(n):
				sum = sum + A[i][k]*B[k][j]
			row.append(sum)
		C.append(row)

print(C)

