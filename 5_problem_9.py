number_of_layers = int(input("Enter the number of layers: "))

current_layer = 1
for i in range(number_of_layers):
	for k in range(number_of_layers - i):
		print(" ", end="")
	for j in range(current_layer):
		print("*", end="")

	current_layer = current_layer + 2
	print("")