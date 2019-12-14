numbers = [1, 2, 6, 5, 8, 4, 11, -1]

for i in range(len(numbers)):
	min_val = numbers[i]
	min_index = i

	for j in range(i, len(numbers)):
		if min_val > numbers[j]:
			min_val = numbers[j]
			min_index = j

	temp = numbers[i]
	numbers[i] = min_val
	numbers[min_index] = temp

print(numbers)