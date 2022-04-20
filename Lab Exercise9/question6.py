class Marks(Exception):
    pass

class Pass(Marks):
    """Congratulations! You are pass"""
    pass

class Fail(Marks):
    """Sorry! You are fail"""
    pass


passing_marks = 33
try:
    m = int(input("Enter the marks : "))

    if m >= passing_marks:
        raise Pass
    elif m < passing_marks:
        raise Fail

except Pass:
    print("PASS")

except Fail:
    print("FAIL")
