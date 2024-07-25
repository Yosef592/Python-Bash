from random import *


def intro():
	print("Rock, Paper, Scissors Game 🎮".center(100, "_"))
	print("")

def body():
	global user, com, computer
	user = input("Enter a choice (rock, paper or scissors): ")
	com = ["rock", "paper", "scissors"]
	computer = choice(com)
	print("")
	print(f"You chose = {user}\nComputer chose = {computer}")
	print("".center(100, '_'))
	print("")
	
def body2():
	if user == "rock" and computer == "rock":
		print("It's the same".center(100, '#'))
	elif user == "rock" and computer == "paper":
		print("😢😢😢 Computer is win 😢😢😢".center(100, '#'))
	elif user == "rock" and computer == "scissors":
		print("🎉🎁🎉 User is win 🎉🎁🎉".center(100, '$'))
	elif user == "paper" and computer == "paper":
		print("It's the same".center(100, '#'))
	elif user == "paper" and computer == "rock":
		print("🎉🎁🎉 User is win 🎉🎁🎉".center(100, '$'))
	elif user == "paper" and computer == "scissors":
		print("😢😢😢 Computer is win 😢😢😢".center(100, '#'))
	elif user == "scissors" and computer == "scissors":
		print("It's the same".center(100, '#'))
	elif user == "scissors" and computer == "rock":
		print("😢😢😢 Computer is win 😢😢😢".center(100, '#'))
	elif user == "scissors" and computer == "paper":
		print("🎉🎁🎉 User is win 🎉🎁🎉".center(100, '$'))

def end():
	print("".center(100, "_"))


intro()
body()
body2()
end()