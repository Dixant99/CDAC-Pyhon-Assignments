no_of_days = int(input("Enter the number pf days in the month(28-31) : "))
Starting_day = int(input("Enter the starting day (0=Sun, 1=Mon,...):"))

print("S  M  T  W  T  F  S")

#print(" "*Starting_day*3, end= "" )
for j in range(Starting_day):
    print("  ",end=" ")
shift = 0

for i in range(1,no_of_days+1):
    if i<10:
        print(i, end="  ")
    else:
        print(i, end=" ")

    shift += 1
    
    count = Starting_day + shift
    if count == 7:
        print()
        shift = 0
        Starting_day = 0
