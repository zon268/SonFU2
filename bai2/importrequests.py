import re
f=open('requests.txt')
Names=[]
mang=[]
for line in f:
	if "POST" not in line and line.endswith("\n"):
		Names.append(line)
print("Header: ",Names)
print(Names[1])
print(Names[6])
print(Names[8])



