def translate(str1):
    str2 = ""
    list1 = list(str1)
    for i in list1:
        if i == "a":
            str2 = str2 + i
        elif i == "e":
            str2 = str2 + i
        elif i == "i":
            str2 = str2 + i
        elif i == "o":
            str2 = str2 + i
        elif i == "u":
            str2 = str2 + i
        elif i == " ":
            str2 = str2+ i
        else:
            swed = i+"o"+i
            str2 = str2 + swed

    return str2


str1 = input("Enter the String: ")
print(translate(str1))
