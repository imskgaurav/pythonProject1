from array import *

arr = array('i', [])
x = int(input("Pls enter size of Arrays"))
print(x)
#Create am Array of n index

for i in range(x):
    num=int(input("Enter Number for Creating Array"))
    arr.insert(i,num)

print(arr)  
#print(arr.length2)

#Find the index of any value 
count =0
val = int(input("Search for Val in Array"))
for i in arr: 
    if val==i:
       print(count)
       break
     
    count+=1        

     
    