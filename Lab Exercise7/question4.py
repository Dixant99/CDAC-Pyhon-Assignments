from datetime import datetime
from time import strptime
date_1 = datetime(2020, 2, 25)
date_2 = datetime(2020, 9, 17)
a=date_2-date_1
a=str(a)
l1=a.split(",")
print(l1[0])
