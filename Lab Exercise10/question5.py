import string
punc = list(string.punctuation)
punc.append(" ")

str1=input("Enter the phrase : ")
str1=str1.lower()

for items in str1:
    if items in punc:
        str1=str1.replace(items,"")

str1=list(str1)


str2 = str1[::-1]

if str1 == str2:
    print("PALINDROME!")
else:
    print("NOT A PALINDROME!")
