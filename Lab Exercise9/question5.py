try:
    denom=0
    if denom == 0:
        raise ValueError("Denominator value 0 is not allowed")
except ValueError as VE:
    print(VE)
