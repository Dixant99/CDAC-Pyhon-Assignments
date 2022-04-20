from datetime import datetime
date="Jul 1 2016 2:43AM"
a=datetime.strptime(date,"%b %d %Y %I:%M%p")
print(a)

