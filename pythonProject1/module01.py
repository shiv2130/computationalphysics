# n = int(input("Enter a number : "))
# s = 0
# i = 0
# while(i<=n):
#     s = s+i
#     i = i+1
# print("sum = ", s)

#Program for finding the factorial of n numbers

n = int(input("Enter a number: "))
f = 1
while n>0:
    f = f*n
    n = n-1
print(f)
