while True: 
    try:
        x=int(input("Enter the value of x : "))
        if x < 0:
            raise ValueError("The given value is inapprppriate")
    except ValueError as VE:
        print(VE)
        break
