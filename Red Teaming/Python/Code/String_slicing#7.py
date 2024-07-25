
# indexing[]        var[start:stop:step]

name1 = "kali linux"

first_name = name1[0:4]
last_name = name1[5:11]
print(first_name)
print(last_name)

name2 = "parrot linux"

f_name = name2[:6]
l_name = name2[7:]
print(f_name)
print(l_name)

name3 = "ubuntu linux"

step = name3[0:12:2]
step2 = name3[0:12:3]
print(step)
print(step2)

name4 = "python for hacker"

step3 = name4[::2]
step4 = name4[::4]
print(step3)
print(step4)


name5 = "josi yosef"

reversed_name1 = name5[::-1]
reversed_name2 = name5[-1:-6:-1]
reversed_name3 = name5[-7::-1]
print(reversed_name1)
print(reversed_name2)
print(reversed_name3)


websit1 = "https://google.com"
websit2 = "https://python.com"

x = websit2[8:-4:]
print(x)


# slice()   is slice(start, stop, step)

websit3 = "https://google.com"
websit4 = "https://python.com"

x = slice(8,-4)

print(websit3[x])


name7 = "hxbno kali"

h = slice(0,10)
f = slice(0,10,4)
print(name7[h])
print(name7[f])