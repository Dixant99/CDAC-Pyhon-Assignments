file= input(r"Enter the PATH : ")
f=open(file,'r')
rev=f.readlines()
list1=list(reversed(rev))
for item in list1:
    print(item,end="")
f.close()
