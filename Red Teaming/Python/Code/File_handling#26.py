                                        #PYTHON FILE HANDLING
                                #ACCESS MODE = 1,read only mode (r)
                                #              2,read and write (r+)        
                                #              3,write (w)
                                #              4,write and read (w+)
                                #              5,append (a)            
                                #              6,append and read (a+)
                                #              7,binary (b)
                                #              8,create (x)
                                #              9,text (t)


# Create a file
#with open('C:\\Users\\pc\\Desktop\\Red Teaming\\Python\\Files\\Test.txt', 'x') as file:
#    file.close()


# write a file
with open('C:\\Users\\pc\\Desktop\\Red Teaming\\Python\\Files\\Test.txt', 'w') as file:
    file.write("parrot os is the best hacking os in the world!!!")


# read a file
with open('C:\\Users\\pc\\Desktop\\Red Teaming\\Python\\Files\\Test.txt', 'r') as file:
    print(file.read())


# append a file
with open('C:\\Users\\pc\\Desktop\\Red Teaming\\Python\\Files\\Test.txt', 'a') as file:
    file.write("\nkali linux is the best os in the parrot!!!!!!")