# index operator [] = gives access to a sepuence's element (str, list, tuples)


name = 'alex Josi!'

if name[0].islower():
    name = name.capitalize()

print(name)
print('\n')

first_name = name[:4].upper()
last_name = name[5:].lower()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)