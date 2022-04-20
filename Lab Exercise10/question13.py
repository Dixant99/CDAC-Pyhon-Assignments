def find_longest_word(list1):
    a=0
    for i in list1:
        if a < len(i):
            a=len(i)
        else:
            continue
    return a


list1 =['ffjh','ufhfd','hhjhjh']
print(find_longest_word(list1))
