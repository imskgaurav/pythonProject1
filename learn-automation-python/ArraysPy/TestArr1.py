import array as myArray

arr= myArray.array('i',[7,8,6])
print(arr.typecode)
print(arr)
print(len(arr))
for i in range(0,len(arr)):
    print(arr[i] , end="  ")


arr1 = myArray.array('d',[9.00,7.00,91.09,-80.8])

for i in range(0, len(arr1)):
    print(arr1[i])

