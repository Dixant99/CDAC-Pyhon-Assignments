def func1():
    try:
        c=5/0
    except ZeroDivisionError:
        print("Sorry! Not divisible by zero")

func1()
