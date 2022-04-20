from datetime import datetime, timedelta
a=input("Enter the year : ")
dates=datetime.strptime(a,"%Y")
count=0
while count<365:
    count+=1
    dates = dates + timedelta(days=1)
    d=dates.strftime("%w")
    if d == '0':
        print(dates)
    else:
        continue
    
