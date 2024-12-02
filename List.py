import sys

myList =[]
print(type(myList))
myList.reverse()
print(myList[:-1])
myList.append(6)
myList.append("GANESH")
myList.append('c')
myList.append(2)
myList.remove(2)

for x in myList:
    print(x)

print(sys.version_info)