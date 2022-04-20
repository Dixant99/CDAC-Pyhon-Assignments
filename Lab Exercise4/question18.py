for a in range(1,11):
    print("\t", a,end=" ")
print()
print("   +",end="")
print(("-")*80)
for i in range(1,11):
    if i<10:
        print (i ," |",end="")
    else:
        print (i ,"|",end="")
    for j in range(1,11):
        print("\t",i*j,end=" ")
    print()
        
