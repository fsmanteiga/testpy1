#!/usr/bin/python3

# Just a quick test
print("[fsmanteiga python tests]")

def printDict(dict):
    for e in dict:
        print(str(e) + " " + str(dict[e]) )

# Declare list
myList=[]

for i in range(0,20):
    print(str(i)+" Added")
    myList.append(i)

# Initialize index i
i = 0
for element in myList:
    print("element "+str(i)+" is : "+str(element))
    i = i + 1

print("**********************")

dic = {}
for i in range(7, 0, -1):
    dic[i] = i*i

printDict(dic)




