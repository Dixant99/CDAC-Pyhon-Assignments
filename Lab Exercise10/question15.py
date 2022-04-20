
def correct(str1):
    if ". " in str1:
        pass
    elif "." in str1:
        str1 = str1.replace(".",". ")
    str1 = str1.replace("  "," ")
    return str1

print(correct("This is very  funny  and cool.Indeed!"))
