def function():
    print("josi")
    print("kali linux is the best!!!")

function()

print("\n")

def func(name):
    print(f"hello {name}")
    print("buy buy")

func("josi")

print("\n")

def name(f_name, l_name):
    print(f_name)
    print(l_name)

name("josi", "alex")

print("\n")

def age(x, y, z):
    print(f"{x} and {y} and {z}")

age("kali", "parrot", 97)



print("\n\n")




# return statment

def mult(no1, no2):
    result = no1 * no2
    return result

x = mult(4, 4)
print(x)




print("\n\n")




# keyword arguments

def key(f_name, l_name):
    print(f_name,l_name)
    
key(l_name="alex" ,f_name="yosef")