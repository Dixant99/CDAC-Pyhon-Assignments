def countLines(name):
    f=open(name,'r')
    f.seek(0)
    list1=f.readlines()
    print("number of lines in the file: ",len(list1))
    f.close()

def countChars(name):
    file=open(name,'r')
    file.seek(0)
    b=file.read()
    d=b.count('\n')
    print("number of chracters in the file:",file.tell()-(2*d))
    file.close()

def test(name):
    countLines(name)
    countChars(name)


if __name__=="__main__":
    name=input(r"Enter the path in the raw path: ")
    countLines(name)
    countChars(name)
    test(name)
else:
    print("mymod is imported") #question3
