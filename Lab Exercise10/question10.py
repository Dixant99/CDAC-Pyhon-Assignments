def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
 
n = int(input("Enter the value of n: "))

if __name__ == "__main__":
    if n>0:
        for i in range(1,n+1):
            print(i,factorial(i))
    else:
        print("Number is less than zero")

    
        
    
