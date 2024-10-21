# a = [10, 15, 89, 50, 25, 20, 110]
# print(a)
def lsearch(x, y):
    # b = int(input("Enter a number you want to search: "))
    for i in range(len(x)):
        if x[i] == y:
            print(y, "found at index: ", i)
            break
    else:
        print("Number not found")
def bsearch(a, b, l, h):
    mid = (l+h)//2
    if l<=h:
        if b == a[mid]:
            print(a[mid], "Number found at index", mid)
        elif b > a[mid]:
            return bsearch(a, b, mid+1, h)
        elif b < a[mid]:
            return bsearch(a, b, l, mid-1)
    else:
        print("Number not found")
def ascend(b):

    for i in range(len(b)):
        for j in range(len(b)-1):
            if b[j] > b[j+1]:
                t = b[j]
                b[j] = b[j+1]
                b[j+1] = t
    for i in range(len(b)):
        print(b[i], end=" ")

def descend(a):

    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] < a[j+1]:
                t = a[j]
                a[j] = a[j+1]
                a[j+1] = t
    for i in range(len(a)):
        print(a[i], end = " ")

# c = [10, 15, 20, 89, 200, 250, 300]

# low = 0
# high = len(a) - 1
# y = int(input("Enter a number you wanted to find: "))
# bsearch(c, y, low, high)