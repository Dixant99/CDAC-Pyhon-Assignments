dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}
l1=[dic2,dic3]
d1={}
for n in range(0,2):
    for key, value in l1[n].items():
       dic1[key]=value
print(dic1)
    
