n = int(input("Enter a number: "))
for i in range(0, n):
    for j in range(0, i+1):
        print(chr(i+65), end=" ")
    print()

n = int(input("Enter a number: "))
for i in range(0, n):
    for j in range(0, i+1):
        print(chr(j+65), end=" ")
    print()
x = 1
n = int(input("Enter a number: "))
for i in range(0, n):
    for j in range(0, i+1):
        x = x + 1
        print(chr(63+x), end=" ")
    print()