# #PROGRAM FOR CONVERTING CELSIUS TO FARENHEIT
# f = float(input(" Enter temperature in celsius "))
# c = ((f-32)/9)
# print("The temperature in fahrenheit is : ", c)
#
# #program for simple interest
# p = float(input("Enter principal: "))
# r = float(input(" Enter rate of interest: "))
# t = float(input("Enter time: "))
# si =(p*r*t)/100
# print("The simple interest: ", si)


# #Program for swapping 2 values with 3rd variable
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# print("Value before exchange: ", a, b)
# c = a
# a = b
# b = c
# print("The exchange value: ", a, b)
#
# #Program for swapping 2 variables without 3rd variable


# #Largest number among two given input number
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# if(a>b):
#     print(a, " is greater than ", b )
# else:
#     print(b, " is greater than ", a)

#largest number among 3 given numbers
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# c = int(input("Enter another number: "))
# if(a>b and a>c):
#     print(a, " is greater")
# elif(b>a and b>c):
#     print(b, "is greater")
# else:
#     print(c, "is greater")

#Given input is even or odd

a = int(input(" Enter a number to check if it's even or odd: "))
if a<0:
    print("Enter positive number")
elif a%2==0:
    print(a, "is even")
else:
    print(a, "is odd")