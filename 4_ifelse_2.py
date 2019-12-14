list1 = [1, 10, 3, 4, 6]

if 3 in list1:
	print("3 is in list.")

if 11 not in list1:
	print("list doesn't contain 11")

variable1 = 4

if list1[3] == variable1:
	print("element in index 3 is equal to variable1")


my_string = "this is an example string"

print(my_string[0])
print(my_string[1])
print(my_string[2])

if "example" in my_string:
	print("example is in my_string variable")

if len(list1) == 5:
	print("Length of the list is 5")

var3 = 3

# all the codes with indent belongs to the section defined above it (if, else or elif)
if var3 < 5:
	var4 = var3 * var3 # or we can write it as var3**2
	var4 = var4 + 1
	print(var4)
else:
	var3 = var3 + 10
	print(var3)
