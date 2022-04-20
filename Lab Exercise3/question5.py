str=input("Enter the word")
if len(str)>3:
    if str[-3:]=='ing':
        print(str[:-3]+'ly')
    else:
        print(str+'ing')
else:
    print("Invalid Input")
