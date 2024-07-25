# scope = local and global variable

# global variable is can used any place
# local variable is can used in localy



name = "josi"       # global variable

def kali():
    name = "yosef"    # local variable
    print(name)

print(name)
kali()



print("\n")



def func():
  global x, a                   # to out a local variable into a globaly
  x = "fantastic"
  a = "awesome"

func()

print(f"Python is {x}")
print(f"Python was {a}")