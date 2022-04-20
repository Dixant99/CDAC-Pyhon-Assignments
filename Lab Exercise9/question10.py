import sys
try:
    x=input("Enter the value of x : ")
    try:
        int(x)
        a=0
    except:
        a=1
        
    if a==1:
        raise TypeError()
    
except TypeError:
    print(sys.exc_info()[0])
