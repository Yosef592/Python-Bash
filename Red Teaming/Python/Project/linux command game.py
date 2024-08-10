# PRINT
print("                                 find the flag")
print("                          Enter best 10 linux comand")
# INPUT
linux0 = input("command 1: ")
linux1 = input("command 2: ")
linux2 = input("command 3: ")
linux3 = input("command 4: ")
linux4 = input("command 5: ")
linux5 = input("command 6: ")
linux6 = input("command 7: ")
linux7 = input("command 8: ")
linux8 = input("command 9: ")
linux9 = input("command 10: ")

# VARYABLE
a = "ls"
b = "cd"
c = "pwd"
d = "clear"
e = "cat"
f = "nano"
g = "curl"
h = "cp"
i = "rm"
j = "mkdir"

# IF STATMENT
if linux0 == a:
    print("true")
else:
    print("false")
if linux1 == b:
    print("true")
else:
    print("false")
if linux2 == c:
    print("true")
else:
    print("false")
if linux3 == d:
    print("true")
else:
    print("false")
if linux4 == e:
    print("true")
else:
    print("false")
if linux5 == f:
    print("true")
else:
    print("false")
if linux6 == g:
    print("true")
else:
    print("false")
if linux7 == h:
    print("true")
else:
    print("false")
if linux8 == i:
    print("true")
else:
    print("false")
if linux9 == j:
    print("true")
else:
    print("false")

# FLAG
if linux0 == a and linux1 == b and linux2 == c and linux3 == d and linux4 == e and linux5 == f and linux6 == g and linux7 == h and linux8 == i and linux9 == j:
    print("                     you flag is = flag{yaoj_ihn42}")
    print(" ")
    inp = input("                     Enter your flag: ")
    if inp == "flag{yaoj_ihn42}":
        print(" ")
        print("                              you win")
    else:
        print(" ")
        print("                              you lose")

else:
    print(" ")
    print("                                   you lose")


# END

