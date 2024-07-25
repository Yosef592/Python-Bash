# computer work with binarys.
# bin(number) = to show you the binary value of your number.
# int('binary no', 2) = to show you the number value of your binary code.
# True = 1
# False = 0

print("9 in binary =",bin(9))
print("0b1001 in number =",int('1001', 2))


# Complement (NOT) (~)
# it will add 1 to the number then makes it negative.

print(~18)


# AND (&)
# bin(7) -> 111, but we can do 0111.
# 10&7=2
# 10 -> 1010
#       &&&&
# 7  -> 0111
#    =  0010 == 2

print(10&7)


# OR (|)
# 10|7=15
# 10 -> 1010
#       ||||
# 7  -> 0111
#    =  1111 == 15

print(10|7)


# XOR(^)
# if they are same = 0   1^1=0,   0^0=0
# if they are different = 1     1^0=1,    0^1=1
# 10^7=13
# 10 -> 1010
#       ^^^^
# 7  -> 0111
#    =  1101 == 13

print(10^7)


# Left Shift(<<)
# 10 << 2 = 40 -> shifting 2 bits to the left.
# 10 -> 1010.0000
#       101000.00
#       101000 == 40

print(10<<2)


# Right Shift(>>)
# 10 >> 2 = 2 -> shifting 2 bits to the Right.
# 10 -> 1010.0000
#       10.100000
#       10 == 2

print(10>>2)