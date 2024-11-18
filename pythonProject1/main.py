# n = int(input("Enter a number: "))
# for i in range(0, n):
#     for j in range(0, i+1):
#         print("*", end = " ")
#     print()

# n = int(input("Enter a number: "))
# if n & 1 == 1:
#     print("Odd number")
# elif n & 1 ==0:
#     print("Even number")


#Find number of armstrong numbers in between 100 and 999

lower = 100
upper = 999

for num in range(lower, upper + 1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print(num)