a= input("Enter the String: ")
b=list(a)
d={}
l1=['a','e','i','o','u']
for j in l1:
    c=b.count(j)
    print("number of", j , "in" , a , "is" ,c)
    d[j]=c
print("\n In Dictonary")
print(d)    
    
