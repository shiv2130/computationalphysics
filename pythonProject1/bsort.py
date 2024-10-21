a = [5, 10, 8, 100, 51, 20, 49, 35, 42]
# for i in range(len(a)):
#     for j in range(len(a)-1):
#         if a[j] > a[j+1]:
#             t = a[j]
#             a[j] = a[j+1]
#             a[j+1] = t
# for i in range(len(a)):
#     print(a[i], end=" ")


for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] < a[j+1]:
            t = a[j]
            a[j] = a[j+1]
            a[j+1] = t
for i in range(len(a)):
    print(a[i], end = " ")
