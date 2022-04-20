from datetime import datetime,timedelta
nxt=datetime.now()
print(nxt.strftime("%Y-%m-%d"))
for i in range(0,9):
    nxt=nxt+timedelta(days=14)
    print(nxt.strftime("%Y-%m-%d"))
