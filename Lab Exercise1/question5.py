import cmath
a= int(input('Enter the value of a'))
b= int(input('Enter the value of b'))
c= int(input('Enter the value of c'))

d1=-b+cmath.sqrt(b**2-4*a*c)/2*a
d2=-b-cmath.sqrt(b**2-4*a*c)/2*a
print(d1)
print(d2)
