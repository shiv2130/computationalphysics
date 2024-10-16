# # Break and continue in python
# #with break
# n = int(input("Enter number rows: "))
# for i in range(0, n+1):
#     for j in range(0, i+1):
#         if(i==2):
#             break
#         print("*", end = " ")
#     print()
#
# #with continue
# n = int(input("Enter number rows: "))
# for i in range(0, n+1):
#     for j in range(0, i+1):
#         if(i==2):
#             continue
#         print("*", end = " ")
#     print()
#
#
# n = int(input("Enter number rows: "))
# for i in range(0, n+1):
#     for j in range(0, i+1):
#         if(j==2):
#             continue
#         print("*", end = " ")
#     print()
#
#
# for val in "string":
#     if val == "i":
#         continue#->generally skips the statement and then return to the for loop
#     print(val)
# print("The end")


# n = int(input("Enter a number to find it's prime or not: "))
# for  i in range(2, n):
#     if (n%i==0):
#         print("Not prime Number")
#         break
# else:
#     print("Prime")


def fact(n):
    if(n<0):
        print("Invalid number")
    elif(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
a = int(input("Enter a number: "))
b = fact(a)
print(b)