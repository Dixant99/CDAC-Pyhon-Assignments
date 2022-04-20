f=open("log.txt",'r')
try:
    f.write("Hi! Show Error")
except:
    print("sorry! You cannot write in this mode")
finally:
    f.close()
