try:
	print(name)
except:
	print("invalid")




try:
	no = 5/0
	print(no)
except ZeroDivisionError:
	print("Can't divide by Zero")




try:
	number = int(input("Enter a number: "))
	print(number)
except ValueError:
	print("Invalid Input")




try:
	name = "kali"
	print(names)
except Exception as x:
	print(x)