name=input(r"Enter the PATH: ")

#to count characters
file=open(name,'r')
b=file.read()
d=b.count('\n')
print("number of characters in the file:",file.tell()-(2*d))

#to count words
file.seek(0)
e=file.read()
g=e.replace('\n',' ')
l1=list(g.split())
print("number of words in the file: ",len(l1))

#to count lines
file.seek(0)
list1=file.readlines()
print("number of lines in the file: ",len(list1))
file.close()


