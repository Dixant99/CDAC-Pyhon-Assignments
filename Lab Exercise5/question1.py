n=int(input("Enter the upto the term you needed Fibonacci sequence: "))
n1=0
n2=1
if n == 1:
    print("0")
elif n == 2:
    print("0",end=" ")
    print("1",end=" ")
else:
    print(n1,end=" ")
    print(n2,end=" ")
    for i in range(0,n-2):
        a=n1+n2
        n1=n2
        n2=a
        print(a,end=" ")
