import random as ra

key_1 = ra.randint(1, 15)
key_2 = ra.randint(1, 15)
key_3 = ra.randint(1, 15)
Guess_1 = int(input("Enter Guessing number_1: "))
Guess_2 = int(input("Enter Guessing number_2: "))
Guess_3 = int(input("Enter Guessing number_3: "))

if Guess_1 == key_1 and Guess_2 == key_2 and Guess_3 == key_3:
    print("you win")
elif Guess_1 == key_1 and Guess_2 != key_2 and Guess_3 != key_3:
    print("Guess_1 = TRUE")
    print("Guess_2 = ",key_2)
    print("Guess_3 = ",key_3)
elif Guess_1 != key_1 and Guess_2 == key_2 and Guess_3 != key_3:
    print("Guess_1 = ",key_1)
    print("Guess_2 = TRUE")
    print("Guess_3 = ",key_3)
elif Guess_1 != key_1 and Guess_2 != key_2 and Guess_3 == key_3:
    print("Guess_1 = ",key_1)
    print("Guess_2 = ",key_2)
    print("Guess_3 = TRUE")
else:
    print("Guess_1 = ",key_1)
    print("Guess_2 = ",key_2)
    print("Guess_3 = ",key_3)