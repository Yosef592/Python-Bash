try:

	inp = int(input("Enter born day: "))
	inp2 = int(input("Enter born year: "))

	if inp < 30:
		inp3 = 2023 - inp2
		print(f"Your age {inp3} years old")
	else:
		inp4 = 2023 - inp2 + 1
		print(f"Your age {inp4} years old")


except Exception as e:
	print(e)
