# While loop = a statement that will execute it's block of code as long as it's condition remains true.

a = 1
while a < 10:
    print(a)
    a += 1

name = ""
while len(name) == 0:
    name = input("Enter your name: ")
print(f"Hello {name}")