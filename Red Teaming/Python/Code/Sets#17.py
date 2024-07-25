# set = collection which is unordered, unindexed. no duplicate values


sets1 = {"kali", "linux", "ubuntu"}
sets2 = {"josi", "yosef", "hxbno"}


sets1.add("parrot")
sets1.remove("linux")
# sets.clear()
sets2.update(sets1)
all_sets = sets1.union(sets2)

for x in sets1:
    print(f"Sets1 == {x}")

print("\n")

for i in sets2:
    print(f"Sets2 == {i}")

print("\n")

for z in all_sets:
    print(f"all_sets == {z}")


print("\n\n")


name = {"abebe", "kebede", "sami"}
name2 = {"robal", "sami", "sutafe"}

print(name2.difference(name))
print(name.intersection(name2))