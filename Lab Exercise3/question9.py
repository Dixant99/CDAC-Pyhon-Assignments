str= input("Enter the word or number")
l1=(list(str))
print(l1)
l2=l1[::-1]
print(l2)
if l1==l2:
    print('Palindrome')
else:
    print('Not a Palindrome')
