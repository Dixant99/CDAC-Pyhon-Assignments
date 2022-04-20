file=input(r"Enter the PATH : ")
f=open(file,'r')
n=int(input("Enter how many lines you want : "))
for i in range(0,n):
    print(f.readline(),end='')
