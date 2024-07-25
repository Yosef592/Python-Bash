# list = used to store multiple item in a single variable

os = ["kali", "linux", "parrot", "ubuntu"]

print(os[1])
os[1] = "Red hat"       # change linux to Red hat
print(os[1])

# os.append("wsl")          ->  add "wsl" in last
# os.remove("ubuntu")       -> remove "ubuntu"
# os.pop()                  -> remove the last item
# os.insert(0, "hashs")     -> add "hashs" on index 0
# os.sort()                
# os.clear()                -> remove all item of the list

for x in os:
    print(x)