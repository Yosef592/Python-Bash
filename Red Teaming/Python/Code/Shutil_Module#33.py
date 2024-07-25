from shutil import *


'''
copy("C:\\Users\\pc\\Desktop\\Red Teaming\\Python\\Files\\Test.txt", "C:\\Users\\pc\\Desktop\\Red Teaming\\Python\\Files\\copy.txt")          # copy a file and save in other plase and other name.
'''


'''
copytree("C:\\Users\\pc\\Desktop\\Red Teaming\\Python\\Files\\jo", "C:\\Users\\pc\\Desktop\\Red Teaming\\Python\\Files\\copydir")       # copy a folder and save in other plase and other name.
'''


'''
def ignore_specific_files(directory, files):
    return [f for f in files if f == "kali.txt"]
        
copytree("C:\\Users\\pc\\Desktop\\Red Teaming\\Python\\Files\\ignore", "C:\\Users\\pc\\Desktop\\Red Teaming\\Python\\Files\\file2", ignore=ignore_specific_files)
# ignore a kali.txt file
'''


'''
def ignore(directory, files):
    return [x for x in files if x.endswith(".txt")]

copytree("C:\\Users\\pc\\Desktop\\Red Teaming\\Python\\Files\\ignore_2", "C:\\Users\\pc\\Desktop\\Red Teaming\\Python\\Files\\file3", ignore=ignore)
# ignore a .txt files
'''


'''
move("C:\\Users\\pc\\Desktop\\Red Teaming\\Python\\Files\\move.txt", "C:\\Users\\pc\\Desktop\\Red Teaming\\Python\\Files\\move_file.txt")       # move a file
'''


'''
rmtree("C:\\Users\\pc\\Desktop\\Red Teaming\\Python\\Files\\del")           #remove a folder
'''


'''
chown("C:\\Users\\pc\\Desktop\\Red Teaming\\Python\\Files\\chown.txt", user='root', group='root')       # change the file owner ship
'''


'''
x = which('python3')            # like a linux which command
print(x)
'''


'''
make_archive('hacker', 'zip', 'josi')           # create a zip file,  you can create a tar,zip... archive
'''


'''
unpack_archive('hacker.zip', 'unzipfile')       # unzip a zip file, you can do in tar,zip.. archive
'''



print(get_archive_formats())                # list a archive
print(get_unpack_formats())