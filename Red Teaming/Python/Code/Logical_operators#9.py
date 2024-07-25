# logical operator (and, or, not) = used to chack if tow or more conditional statment is true


temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("the temperature is good")
elif temp < 0 or temp > 30:
    print("the temperature is bad")


print("\n")

temp2 = int(input("What is the temperature outside?: "))

if not(temp2 >= 0 and temp2 <= 30):
    print("the temperature is bad")
elif not(temp2 < 0 or temp2 > 30):
    print("the temperature is good")