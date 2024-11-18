# Str1 = "Bhopal"
# for i in Str1:
#     print(i, end = " ")



# for i in range(0, 11):
#     print(i)

#program for finding out
# n = int(input("Enter a number: "))
# f = 1
# for i in range(1, n+1):
#     f = f*i
# print(f)

#program for printing star pattern

# n = int(input("Enter number rows: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print("*", end = " ")
#     print()

#program for printing pattern
#
# n = int(input("Enter number of rows: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end = " ")
#     print()

#Program for printing another number pattern

# n = int(input("Enter number of rows: "))
# for i in range(1, n+1):
#     for j in range(i, n+1):
#         print("*", end = " ")
#     print()

# #printing another number pattern
# n = int(input("Enter number of rows: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j,  end = " ")
#     print()
#
#printing another number pattern
n = int(input("Enter a number of rows: "))
x = 0
for i in range(n):
    for j in range(i):
        x = x + 1
        print(x, end = " ")

    print()
#n = int(input("Enter a number: "))
# a = n
# s = 0
# while a>0:
#     x = a % 10
#     a = a // 10
#     s = s + x * x * x
# if n == s:
#     print("Armstrong number", n)
# else:
#     print("Not armstrong")

# s = 0
# a = n
# while(n>0):
#     x = n%10
#     n = n//10
#     s = s*10+x
# if(a == s):
#     print(a, "Palindrome number")
# else:
#     print(a, "Is not a palindrome number")
# a, b = 0, 1
# count = 0
# if n<=0:
#     print("Enter a positive number: ")
# elif n==1:
#     print("Fibonacci sequence upto: ", n, ":")
#     print(a)
# else:
#     print("Fibonacci sequence:")
#     while count < n:
#         print(a, end = " ")
#         nth = a + b
#         # update values
#         a = b
#         b = nth
#         count += 1
