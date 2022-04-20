file=input(r"Enter the raw PATH : ")
f = open(file,'a')
f.write("\nnew line is added from question 9")

f.close()

f=open(file,'r')
print(f.read())
f.close()
