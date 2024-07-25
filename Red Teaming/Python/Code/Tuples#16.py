# tuple = collection which is ordered and unchangable, used to group together related data


student = ("bro", 12, "josi")

print(student.count("josi"))
print(student.index("bro"))
print("\n")

for x in student:
    print(x)

print("\n")

if "josi" in student:
    print("josi is here!")