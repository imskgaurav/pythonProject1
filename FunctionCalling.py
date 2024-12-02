def addition(a, b):
    result = a + b
    return result


def multiplication(x, y):
    result = x * y
    return result

print(addition((multiplication(5,7)), 9))

def square(num):
    return num*num

n1= square(3)
print(n1)

#Create a numbers List #
numbers =[1,2,3,4]

#SQAURE all the Number in the list 
square_list = map(square,numbers)

print(square_list)

#Convert Map into list 
result = list(square_list)
print(result)



