x=int(input("Enter upto which term : "))
a=[]
for i in range(1,x+1):
    a.append(i)
b=list(map(lambda x:2**x,a))
print(b)
