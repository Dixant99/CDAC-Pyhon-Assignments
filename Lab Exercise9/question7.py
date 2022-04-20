"""To see another error message put "#" on print(a)"""
try:
    print(a) #NameError
    a=5/0 #ZeroValueError
    
except NameError:
    print("This message is shown in case of Name Error")

except:
    print("Another Error Message")
