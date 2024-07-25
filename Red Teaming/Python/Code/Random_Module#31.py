from random import *


x = random()   # random floting point number.
print(x)

y = uniform(1, 10)  # random floting point in 1 - 10.
print(y)

z = randint(1, 9)  # random int in 1 - 9.
print(z)

os = ["kali", "ubuntu", "parrot"]
a = choice(os)   # choice random words from os list.
print(a)

colors = ["Red", "Black", "Green"]
b = choices(colors, weights=[18, 18, 2])    # less chanse of Green.
print(b)

number = list(range(1, 100))
h = sample(number, k=5)     # choice a 5 character or number.
print(h)