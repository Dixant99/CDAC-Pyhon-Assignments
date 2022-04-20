n=int(input("Enter the number upto which you need sum : "))
def natural_sum(n):
    if n==1:
        return 1
    else:
        return n + natural_sum(n-1)
print(natural_sum(n))
