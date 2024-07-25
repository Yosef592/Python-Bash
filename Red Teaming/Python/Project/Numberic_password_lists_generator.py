from time import *

def intro():
    print("")
    print("WELCOME TO P@CR7".center(100, "_"))
    print("")
    print("P@CR7 is generat a numberic password lists.".center(100, "~"))
    print("start with 2 digits, end with 9 digits.".center(100, "~"))
    print("")
    print("DEVELOPED BY ^HXBNO^".center(100))
    print("".center(100, "_"))
    sleep(3)
    print("")

def body():
    global inp
    inp = input("Enter a digit (2 - 9)\n>> ")
    print("\n")
    print("Please Wait...")
    print("\n")
    sleep(2)

def body2():
    if inp == "2":
        p2()
    elif inp == "3":
        p3()
    elif inp == "4":
        p4()
    elif inp == "5":
        p5()
    elif inp == "6":
        p6()
    elif inp == "7":
        p7()
    elif inp == "8":
        p8()
    elif inp == "9":
        p9()
    else:
        print("Something is wrong")

def p2():
    with open('Password_list_2.txt','x') as file:
       file.close()
    with open('Password_list_2.txt', 'w') as file:
       for i in range(100):
          password = f"{i:02}"
          file.write(password + '\n')
    print("SAVE TO 'Password_list_2.txt'")
def p3():
    with open('Password_list_3.txt','x') as file:
       file.close()
    with open('Password_list_3.txt', 'w') as file:
       for i in range(1000):
          password = f"{i:03}"
          file.write(password + '\n')
    print("SAVE TO 'Password_list_3.txt'")

def p4():
    with open('Password_list_4.txt','x') as file:
       file.close()
    with open('Password_list_4.txt', 'w') as file:
       for i in range(10000):
          password = f"{i:04}"
          file.write(password + '\n')
    print("SAVE TO 'Password_list_4.txt'")

def p5():
    with open('Password_list_5.txt','x') as file:
       file.close()
    with open('Password_list_5.txt', 'w') as file:
       for i in range(100000):
          password = f"{i:05}"
          file.write(password + '\n')
    print("SAVE TO 'Password_list_5.txt'")

def p6():
    with open('Password_list_6.txt','x') as file:
       file.close()
    with open('Password_list_6.txt', 'w') as file:
       for i in range(1000000):
          password = f"{i:06}"
          file.write(password + '\n')
    print("SAVE TO 'Password_list_6.txt'")
def p7():
    with open('Password_list_7.txt','x') as file:
       file.close()
    with open('Password_list_7.txt', 'w') as file:
       for i in range(10000000):
          password = f"{i:07}"
          file.write(password + '\n')
    print("SAVE TO 'Password_list_7.txt'")

def p8():
    with open('Password_list_8.txt','x') as file:
       file.close()
    with open('Password_list_8.txt', 'w') as file:
       for i in range(100000000):
          password = f"{i:08}"
          file.write(password + '\n')
    print("SAVE TO 'Password_list_8.txt'")
def p9():
    with open('Password_list_9.txt','x') as file:
       file.close()
    with open('Password_list_9.txt', 'w') as file:
       for i in range(1000000000):
          password = f"{i:09}"
          file.write(password + '\n')
    print("SAVE TO 'Password_list_9.txt'")

def end():
    print("\n")
    print(" Thank you from using this tool. ".center(100, "$"))
    print("Developed in 6/27/2024".center(100))
    print("\n")



intro()
body()
body2()
end()