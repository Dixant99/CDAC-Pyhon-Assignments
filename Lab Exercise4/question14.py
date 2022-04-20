import string
punc=(string.punctuation)


istr= input("Enter the string: ")

new ="  "

for i in istr:
    if i not in punc :
        new += i
print(new)
