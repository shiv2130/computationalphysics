import linear_Search as l
while True:
    print("1. Linear search")
    print("2. Binary search")
    print("3. Exit")
    c = int(input("Enter choice: "))
    if c == 1:
        a = [10, 15, 89, 50, 25, 20, 110]
        print(a)
        b = int(input("Enter a number you want to search: "))
        l.lsearch(a,b)
    elif c == 2:
        d = input("The array is sorted(Y/N): ")
        if d == "Y" or d == "y":
            w = [10, 15, 20, 25, 50, 89, 110]
            print(w)
            low = 0
            high = len(w) - 1
            y = int(input("Enter a number you wanted to find: "))
            l.bsearch(w, y, low, high)
        else:
            print("Sort the array first")
            break
    elif c == 3:
          print("Thank you")
          break

    p = input("Do you wish to continue(Y/N): ")
    if p == "N" or p == "n":
        print("Thank You!")
        break




