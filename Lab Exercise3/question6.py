print("Marks must be out of 100")
a= float(input('Enter Subject 1 marks'))
b= float(input('Enter Subject 2 marks'))
c= float(input('Enter Subject 3 marks'))
d= float(input('Enter Subject 4 marks'))
e= float(input('Enter Subject 5 marks'))

A = ((a+b+c+d+e)/5)#percentage

print("Your percentage is ", A ,'%')

if ( A >= 60):
    print("First Division")
elif(A < 60 and A >= 50):
    print("Second Division")
elif(A < 50 and A >= 40):
    print("Third Division")
else:
    print("FAIL")
