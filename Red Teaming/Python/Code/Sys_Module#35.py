from sys import *


filename = argv[0]          # display a file name.
print(filename)
print('\n')

name = argv[1]          # input in terminal like this " python3 file.py josi ".
age = int(argv[2])      # input in terminal like this " python3 file.py 97 ".    
print(f"Hello {name}.\nyou are {age} years old.\n")

system_info = platform      # to find a using os system.
print(system_info)

python_versions = version          # to find a python version.
print(python_versions)

exit()          # stop(exit) a sys module.