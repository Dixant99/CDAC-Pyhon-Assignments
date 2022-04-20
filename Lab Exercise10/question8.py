people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
print(people)
"""1. Find out how many students are in the list"""

count = 0
for i in people:
    count += 1
    
print(count)
"""2. Change Lisa’s favourite colour"""
colour = input("Enter Lisa's favourite colour: ")
people['Lisa'] = colour
print(people)
"""3. Remove 'Jenny' and her favourite colour"""
people.pop('Jenny')
print(people)

people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
"""4. Sort and print students and their favourite colours alphabetically by name"""
list1=[]
for keys,value in people.items():
    list1.append(keys)
list1.sort()

peoples={}
for i in list1:
    peoples[i]= people[i]
print(peoples)
