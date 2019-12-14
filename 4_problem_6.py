import math

grade = 90
adjusted_grade = 10 * math.sqrt(grade)

if adjusted_grade >= 90:
	print("AA")
elif adjusted_grade < 90 and adjusted_grade >= 85:
	print("BA")
elif adjusted_grade < 85 and adjusted_grade >= 80:
	print("BB")
elif adjusted_grade < 80 and adjusted_grade >= 75:
	print("CB")
elif adjusted_grade < 75 and adjusted_grade >= 70:
	print("CC")
elif adjusted_grade < 70 and adjusted_grade >= 65:
	print("DC")
elif adjusted_grade < 65 and adjusted_grade >= 60:
	print("DD")
elif adjusted_grade < 50 and adjusted_grade >= 55:
	print("FD")
else:
	print("FF")

