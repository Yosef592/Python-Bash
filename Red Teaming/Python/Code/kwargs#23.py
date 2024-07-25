# **kwargs = parameter that will pack all argument into a dictionary.
# useful so that a function can accept a varying amount of keyword arguments


def hello(**name):
    print("hello", end=" ")
    for key,value in name.items():
        print(value, end=" ")

hello(name1="josi", name2="kali", name3="parrot")