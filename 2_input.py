var = input("Please write input")
print(var)

var1 = input("Enter the first integer")
var2 = input("Enter the second integer")

#below will not run, we need casting
print(var1 + var2)
print(type(var1))

print(int(var1) + int(var2))
var2 = int(var1)
print(type(var2))
