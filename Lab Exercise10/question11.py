def main(n):
    for i in range(1,n):
        print(str(i) + " + ",end="")
    print(n,end=" = ")

def sum(x):
# you complete this function recursively main()
    if x==1:
        return 1
    else:
        return x + sum(x-1)
x= int(input("Enter the value: "))
main(x)
print(sum(x))
