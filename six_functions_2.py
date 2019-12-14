def square(number):
	return number**2

def sort(numbers):

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

	return numbers

def f(arg1, arg2, arg3, arg4=2):
	print("This is arg1: " + str(arg1))
	print("This is sum of arg2 and arg3: " + str(arg2+arg3))
	print("This is arg4:" + str(arg4))

def side_effect_func():
	list1.pop(0)

var1 = 2
squared = square(var1)
print(squared)

list1 = [0 , 4, -3, 2, 7, 1]
print(sort(list1))

f(1, 2, 5)

print(list1)
side_effect_func()
print(list1)
