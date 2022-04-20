file=input(r" Enter the raw path of the file : ")
lines=['\nfirst line','\nsecond line','\nthird line']
print(lines)

f=open(file,'a+')
f.writelines(lines)
f.seek(0)
print(f.read())
f.close()
