import numpy as np
import random

A = [[1,2,3],
	 [4,5,6],
	 [7,8,9],
	 [10,11,12]]

B = [[1,0,0,1],
	 [0,1,0,1],
	 [0,0,1,0]]

print(type(A))
print(type(B))


A = np.asarray(A)
B = np.asarray(B)

print(type(A))
print(type(B))

print(np.cos(30))
print(np.sin(30))
print(np.exp(2))
print(np.pi)
print(np.square(2))
print(np.sqrt(9))
print(np.dot(A, B))
print(np.shape(A))
print(np.argmax(A[3]))
print(np.ceil(0.3))

print(random.random())
prob = random.random()

if prob <= 0.7:
	print("Head")
else:
	print("Tail")

