list1 = []

for i in range(97,123):
    a = chr(i)
    list1.append(a)


str1 = input("Enter the sentence : ")
str1 = str1.lower()

for j in range(0,len(str1)):
    x = str1[j]

    if x in list1:
        list1.remove(x)

    else:
        continue


if list1 == []:
    print("Yes! It is Panagram")
else:
    print("NOT a Panagram ")


