file=input(r"Enter the raw PATH : ")
f = open(file,'r')
c=f.read()
list1=c.split("\n")
for item in list1:
    print(item)
print(list1)
f.close()

