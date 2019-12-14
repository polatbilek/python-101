var1 = 6
var2 = 3

if var1 >= 10:
	print("Bigger than 10") #mind about the indent here (can be created by pressing tab button)
else:
	print("Smaller or equal to 10") # all the codes written under a section wth tab belongs to that section


if var1 == var2:
	print("var1 and 2 are equal")
else:
	print("not equal")


if var1 > 5 and var1 < 7:
	print("Between")
elif var1 <= 5:
	print("Smaller than 5")
else:
	print("Bigger than or equal to 7")

if var1 > 5:
	if var2 < 5:
		print("in good condition")
	else:
		print("var2 breaks the condition")
else:
	print("var1 breaks the condition")