num_1 = int(input("Enter frist num: "))
op = input("Enter oprater: ")
num_2 = int(input("Enter second num: "))

if op == "+":
    print(num_1 + num_2)
elif op == "-":
    print(num_1 - num_2)
elif op == "*":
    print(num_1 * num_2)
else:
    if op == "/":
        print(num_1 / num_2)