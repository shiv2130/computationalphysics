def bsearch(a, b, l, h):
    mid = (l+h)//2
    if l<=h:
        if b == a[mid]:
            print(a[mid], "Number found at index", mid)
        elif b > a[mid]:
            print(bsearch(a, b, mid+1, h))
        elif b < a[mid]:
            print(bsearch(a, b, low, mid-1))
    else:
        print("Number not found")


c = [10, 15, 20, 89, 200, 250, 300]

low = 0
high = len(c) - 1
y = int(input("Enter a number you wanted to find: "))
bsearch(c, y, low, high)