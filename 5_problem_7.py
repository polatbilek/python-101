list1 = [0, -1, 3, 5, 10, 2, 1, 7]

max_index = 0
max_value = list1[max_index]

for i in range(len(list1)):
	if max_value < list1[i]:
		max_index = i
		max_value = list1[i]

print(max_index)