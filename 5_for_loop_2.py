new_list = [1, 2, -1, 0, 5, -10]
for elem in new_list:
	if elem == 0:
		break
	else:
		print(elem)

list1 = []

print(list1)
for number in range(20):
	if number > 10 and number <= 15:
		list1.append(number)

print(list1)

for i in range(10):
	var1 = 2
	print(i * var1)

how_many_times = [2, 1, 3]

for repetition in how_many_times:
	for times in range(repetition):
		print(str(times) + " Python")

	print("------")

# Below is problematic code, dont use like this
# It deletes elements from the list we go through so list shrinks while we scan it
# for elem_index in range(len(list1)):
# 	print(list1.pop(elem_index))

