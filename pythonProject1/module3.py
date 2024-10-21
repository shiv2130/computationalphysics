def prime(n):
  for i in range(2, n):
    if (n%i==0):
        print("Not prime Number")
        break
  else:
     print("Prime")
def armstrong(n):
    a = n
    s = 0
    while a > 0:
        x = a % 10
        a = a // 10
        s = s + x * x * x
    if n == s:
        print("Armstrong number", n)
    else:
        print("Not armstrong")

def palindrome(n):
    s = 0
    a = n
    while(n>0):
        x = n%10
        n = n//10
        s = s*10+x
    if(a == s):
        print(a, "Palindrome number")
    else:
        print(a, "Is not a palindrome number")
def fib(n):
    a, b = 0, 1
    count = 0
    if n <= 0:
        print("Enter a positive number: ")
    elif n == 1:
        print("Fibonacci sequence upto: ", n)
        print(a)
    else:
        print("Fibonacci sequence:")
        while count < n:
            print(a)
            nth = a + b
            a = b
            b = nth
            count += 1


