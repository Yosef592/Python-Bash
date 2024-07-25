from os import *


'''
pwd = getcwd()      # display a curent working folder
print(pwd)
'''


'''
chdir("C:\\Users\\pc\\Desktop\\")           # change a folder
'''


'''
ls = listdir()         # list a files or a folders
print(ls)
'''


'''
mkdir("josi")                # create a single folder
makedirs("kali/linux")       # create a multiple folder
'''


'''
rmdir('josi')               # remove a single folder
removedirs('kali/linux')    # remove a multiple folder
'''


'''
rename('kali.txt', 'parrot.txt')       # rename a files or a folders
'''


'''
mb = stat('parrot.txt').st_size      # to find a file size in mb
print(mb)
'''


''' 
for dirpath, dirnames, filenames in walk('C:\\Users\\pc\\Desktop\\'):        # like a linux 'ls -R' command
    print(f"dirpath = {dirpath}")
    print(f"dirnames = {dirnames}")
    print(f"filenames = {filenames}")
    print('\n')
'''


'''
env = environ.get("HOME")       # to find a home directory location
print(env)
'''


'''
x = path.join(environ.get("HOME"), 'kali.txt')
print(x)
'''


'''
ex = path.exists("/home/kali")      # to chacke this directory is live in my system
print(ex)
'''


'''
folder = path.isdir('C:\\Users\\pc\\Desktop')            # chacke is a folder
print(folder)

files = path.isfile('C:\\Users\\pc\\Desktop\\parrot.txt')       # chacke is a file
print(files)
'''


'''
x = path.split('C:\\Users\\pc\\Desktop\\parrot.txt')        # separat a folder name and file name
print(x)
'''


'''
x = path.splitext("C:\\Users\\pc\\Desktop\\parrot.txt")       # separat a file name and extanstion
print(x)
'''


'''
p = path.getsize("C:/Users/pc/Desktop/parrot.txt")      # to find a file size in mb
print(p)
'''


'''
remove("C:/Users/pc/Desktop/parrot.txt")         # remove a file
'''



system("notepad")          # run a terminal command here