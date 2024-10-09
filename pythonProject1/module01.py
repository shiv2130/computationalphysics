# n = int(input("Enter a number : "))
# s = 0
# i = 0
# while(i<=n):
#     s = s+i
#     i = i+1
# print("sum = ", s)

#Program for finding the factorial of n numbers

# n = int(input("Enter a number: "))
# f = 1
# while n>0:
#     f = f*n
#     n = n-1
# print(f)

#Program to reverse a given integer number

# n = int(input("Enter a number: "))
# s = 0
# while n>0:
#     x = n%10
#     s = 10*s+x
#     n = n//10
#     n = n+1
# print(s)

#Printing patterns


# n  = int(input("Enter number of rows: "))
# i = 1
# while(i<=n):
#     j = 1
#     while(j<=i):
#         print(" * ", end = " ")
#         j = j + 1
#     i = i+1
#     print()

n  = int(input("Enter number of rows: "))
i = 1
while(i<=n):
    j = 1
    while(j<=i):
        print(j , end = " ")
        j = j + 1
    i = i+1
    print()

n = int(input("Enter a number: "))
i = 1
while(i<=n):
    j = 1
    while(j<=i):
        print(i, end = " ")
        j = j+1
    i = i+1
    print()

n = int(input("Enter a number: "))
i = 1
x = 1
while(i<=n):
    j = 1
    while(j<=i):
        print(x, end = " ")
        j = j+1
        x = x + 1
    i = i+1
    print()