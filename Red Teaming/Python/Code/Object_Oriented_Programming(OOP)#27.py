'''
class student:
    def intro(self):
        print("Hello",self.name)


s1 = student()
s1.name = "kali"
s1.age = 97

s2 = student()
s2.name = "parrot"
s2.age = 79

s1.intro()
s2.intro()

'''



class student:
    def __init__(s, name, age):
        s.name = name
        s.age = age
    def intro_self(s):
        print("my name is", s.age)



s3 = student("hxbno", 97)
s4 = student("josi", 90)

s3.intro_self()
s4.intro_self()