import module3 as m
while True:
    print("1. Prime Number")
    print("2. Armstrong")
    print("3. Palindrome")
    print("4. Fibonacci")
    print("5. Exit")
    c = int(input("Enter your choice from the above given option: "))
    if c==1:
        a = int(input("Enter a number to find prime number: "))
        m.prime(a)
    elif c==2:
        a = int(input("Enter a number to find armstrong number: "))
        m.armstrong(a)
    elif c==3:
        a = int(input("Enter a number to find Palindrome: "))
        m.palindrome(a)
    elif c==4:
        a = int(input("Enter a number to find fibonacci: "))
        m.fib(a)
    else:
        break

