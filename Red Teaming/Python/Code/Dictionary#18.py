# dictionary = a changeable, unordered collection of unique key:value pairs fast because the hashing, allow us to access a value quickly


user_and_password = {"kali":1297, "Telegram":"josi", "tiktok":9712.8}

print(user_and_password)
print(user_and_password["kali"])
print(user_and_password["Telegram"])
print(user_and_password["tiktok"])
print("\n")
print(user_and_password.get("hxbno"))
print(user_and_password.keys())
print(user_and_password.values())
print(user_and_password.items())

print("\n")

for key,value in user_and_password.items():
    print(f"{key} = {value}")

print('\n')

dic = {'tool':'hydra', 'os':'linux'}

dic.update({'command':'htop'})
dic.update({'tool':'burp'})

for k,v in dic.items():
    print(k, v)

print('\n')
dic.pop('tool')
# dic.clear()

print(dic.items())