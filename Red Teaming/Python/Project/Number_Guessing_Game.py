from random import *

def intro():
    print("Number Guessing Game 🎮".center(100, '_')); print("")

try:
    def game():
        for i in range(5):
            inp = int(input("Guess a number 0 - 9\n>> "))
            if inp == randint(0, 9):
                print("".center(105, "_")); print(""); print(" 🎉🎁🎉 YOU GOT IT 🎉🎁🎉 ".center(100, "$"))
                print("".center(105, "_")); print("")
                break
            elif inp != randint(0, 9):
                print("NO\n")
        print("\n")
except Exception as x:
    print(x)
    
intro(); game()