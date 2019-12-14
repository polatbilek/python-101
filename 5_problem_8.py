limit = int(input("Enter the number of fibonacci number you want: "))

prev_number = 0
current_number = 1

print(str(prev_number) + ", " + str(current_number) + ", ", end="")

for i in range(limit-2):
	next_number = prev_number + current_number
	prev_number = current_number
	current_number = next_number
	print(str(next_number) + ", ", end="")
