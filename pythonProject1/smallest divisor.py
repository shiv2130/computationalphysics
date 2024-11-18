n = int(input("Enter a number: "))
m = int(input("Enter another number: "))
for i in range(2, m):
    if m%i==0:
       if n%i==0:
           print("smallest divisor", i)
           break

