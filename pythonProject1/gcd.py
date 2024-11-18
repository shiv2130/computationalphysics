n = int(input("Enter a number: "))
m = int(input("Enter a number: "))
# while(m):
#     n, m = m, n%m
# print(n)
for i in range(n, 1, -1):
    if n%i==0:
        if m%i==0:
            print("GCD is: ", i)
            break