# *args = parameter that will pack all arguments into a tuple. 
# useful so that a function can accept a varying amount of arguments


def add(*ad):
    sum = 0
    for i in ad:
        sum += i
    return sum

print(add(2, 3, 5, 9))