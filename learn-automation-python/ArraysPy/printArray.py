import array as ar
num = ar.array('i',[1,3,4,2,5,6])
print(num)
i=0
for x in num:
    print(num[i], end="    ")
    i=i+1
#Adding element in the between//
num.insert(0,786)
for i in range(0, len(num)):
    print( num[i])
#append Function to add the element in last 
num.append(777)
print(num, end =" ")
x = list(range(0,20))
print(x)
#copy array 
print('copy Array')
newArr = ar.array(num.typecode, (i for i in num))
print(newArr)
def fun():
    return
print(fun())

# print array value without using index #

for x in num:
    print(x)
    
#Print Array using index of Array 
 
for i in range(len(num)):
    print(num[i])
