# made factorial program without using module
def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    print("Factorial = ", f)
def funr(n):
    if(n<0):
        print('Invalid Number')
    elif(n==0 or n==1):
        return 1
    else:
        return n*funr(n-1)
# a = int(input("Enter a number: "))




