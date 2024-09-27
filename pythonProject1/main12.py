'''
a = 0b111
print(type(a))
print(a)
#using octal number
b = 0o172
print(b)
#hexa-decimal number
c = 0X12A
print(c)
a = 0b1010
b = 0o172
c = 0X12A
d = 10
e = b + c
f = bin(e)
g = bin(c)
print(g)
print(f)
print(e)
'''
#String and it's operation
# string1 = "Welcome to VIT BHOPAL"
# print(string1)
# print("Hello this is the use of string")
# s = "Swarit"
# len(s)
# c = s[-1]
# print(c)
# d = s[0:2]
# print(d)
# str1 = "VitBhopal University"
# e = str1[-10]
# #reint(e)
# print(string1*2)
# #Real part could be binary/octa/hexa or any integer type but the imaginary type should be an pure integer/number
# a  = 0o56 + 23.5j
# b =  0xA2 - 5j
# s = 0b1111
# print(s)
# i = complex(10)
# print(i)
# j = str(10)
# print()
# a = 15
# b = 20
# print("Before exchange: ")
# print(a, b)
# #
# # c = a
# # a = b
# # b = c
# # print("After exchange: ")
# # print(a, b)
# a = a + b
# b = a - b
# a = a - b
# print("After exchange: ")
# print(a, b)
a = 10
b = 15
c = 20
w = a>b and b<a
print(w)
x = a<b and b<c
print(x)
y = a>b or b>c
print(y)
z = a<b or b<c
print(z)
print(not a)
