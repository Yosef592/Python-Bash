# loop control statements = change a loop execution from it's normal sequence

# brack = used to terminate the loop entirely.
# continue = skips to the next iteration of the loop.
# pass = dose nothing, acts as a placeholder.


while True:
    name = input("Enter your name: ")
    if name != "":
        print(f"Hello {name}")
        break

print("\n")

No = "123-456-7890"

for i in No:
    if i == "-":
        continue
    print(i, end="")

print("\n")


for j in range(1, 21):
    if j == 13:
        pass
    else:
        print(j)


print("\n")

number = "12-34-56-789"
for z in number:
    if z == "-":
        pass
    else:
        print(z, end="")