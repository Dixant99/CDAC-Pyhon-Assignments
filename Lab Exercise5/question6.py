def convert(n):
    if n>=1:
        convert(n//2)
    print(n%2,end= '')
       
a=int(input("Enter the number whose binary required: "))
convert(a)
