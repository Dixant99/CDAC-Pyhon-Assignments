def overlapping(list1,list2):
    list3=[]

    for i in list1:
        if i in list2:
            list3.append("True")
        else:
            list3.append("False")


    if "True" in list3:
        return True

    elif "False" in list3:
        return False

#Example True
list1=[1,2,3,4,5]
list2=[5,6,7,8,9]

print(overlapping(list1,list2))

#Example False
list1=[1,2,3,4,5]
list2=[6,7,8,9]

print(overlapping(list1,list2))
