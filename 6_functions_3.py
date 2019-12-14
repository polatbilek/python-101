from six_functions_2 import sort

def another_func(var):
	print(var)
	my_list = [6, 3, 0, 7, -1]
	print(sort(my_list))
	print(my_list)

def called_func(var):
	v2 = var**2
	v2 = v2 - 1
	return v2

def callee_func():
	my_var = 5
	my_var = called_func(my_var)
	return my_var

def multiple_return(my_list):
	var1 = my_list[0]**2
	var2 = my_list[1]**2

	return var1, var2

if __name__ == "__main__":
	print("Always this is printed")
	print("Because main is always executed first")
	#another_func(3)
	#print(callee_func())

	ret1, ret2 = multiple_return([1, 3, 0, 6, 5])
	print(str(ret1) + "   " + str(ret2))    

# and try some mutual exclusion on variables