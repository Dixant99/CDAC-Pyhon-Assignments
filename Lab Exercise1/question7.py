n = int(input('Enter the 5 line number'))
a = n%100000

n=n-10000
b= n%10000

n=n-10000
c= n%1000

n=n-100
d= n%100

n=n-10
e= n%10




a=int((a-b)/10000)

b=int((b-c)/1000)

c=int((c-d)/100)

d=int((d-e)/10)


sum= a+b+c+d+e

print(sum)
