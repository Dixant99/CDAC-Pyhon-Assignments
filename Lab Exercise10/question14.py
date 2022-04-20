def find_longest_word(n,list1):
    list2 = []

    for i in list1:
        if len(i)>= n:
            list2.append(i)
        else:
            continue
    return list2

n=int(input("Enter length of word is upto: "))
list1 =['ffjh','ufhfd','hhjhjh']
print(find_longest_word(n,list1))
