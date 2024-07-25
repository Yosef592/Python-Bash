def intro():
	print("Quiz_Game 🎮".center(100, '_'))
	print("\n")

def body():
	global quiz, answer_list, choise, error
	quiz = ["1, who was the best hacker in the world?",  "2, what is the best programming language in the world?",  "3, what is the best hacker group in the world?",  "4, which one of the following is ethiopian hacker?"]

	answer_list = ["A, Linus Torvalds.\nB, Greg Hoglund.\nC, Kevin Mitnick.\nD, Loyd Blankenship.",
	                "A, C++.\nB, Python.\nC, java.\nD, PHP.", "A, Vice Society.\nB, Royal.\nC, Black Basta.\nD, Anonymous.", "A, Paulos Yibelo.\nB, Kevin Mitnick.\nC, Linus Torvalds.\nD, Nathan Hailu."]

	choise = "Enter your answer (A, B, C or D): "

	error = ["wrong! the correct answer was C ", "wrong! the correct answer was B", "wrong! the correct answer was D", "wrong! the correct answer was A"]


def body2():
	global score
	score = 0
	print(quiz[0])
	print(answer_list[0])
	print("")
	x = input(choise)
	if x == "c" or x == "C":
		print("Correct")
		score += 1
	else:
		print(error[0])
	print("\n")
	print(quiz[1])
	print(answer_list[1])
	print("")
	y = input(choise)
	if y == "b" or y == "B":
		print("Correct")
		score += 1
	else:
		print(error[1])
	print("\n")
	print(quiz[2])
	print(answer_list[2])
	print("")
	z = input(choise)
	if z == "d" or z == "D":
		print("Correct")
		score += 1
	else:
		print(error[2])
	print("\n")
	print(quiz[3])
	print(answer_list[3])
	print("")
	a = input(choise)
	if a == "a" or a == "A":
		print("Correct")
		score += 1
	else:
		print(error[3])
	print("\n")


def finis():
	print(f"You got {score} of 4 questions correct.")
	print("")
	print("Game_Over 🕹".center(100, '_'))



intro()
body()
body2()
finis()