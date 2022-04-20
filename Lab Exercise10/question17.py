IP = input("Enter the IP address: ")

list1=list(IP)

a = IP.count("0")

for i in range(0,a):
    list1.remove("0")

new_IP = ""

for j in list1:
    new_IP += j


print(new_IP)

