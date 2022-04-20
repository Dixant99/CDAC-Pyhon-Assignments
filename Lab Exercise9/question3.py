"""This Program can get exception for ZeroDivisionError, NameError & TypeError.
To check other kind of exception put "#" on other lines.
currently the program is giving output for first line in try clause"""
import sys
try:
    x=5/0 #ZeroDivisionError
    cdac = noida #NameError
    a= 44 + "anything" #TypeError
    

except (ZeroDivisionError, NameError, TypeError):
    print("There is error :", sys.exc_info()[0])
