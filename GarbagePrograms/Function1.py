def simpleFucntion():
    print("Hello Welcome")
    print("Hello World")
simpleFucntion()
print()

def addTwoNumber(x,y=99):
    sum=x+y
    return sum

s=addTwoNumber(66)
print(s)

def sqauare(n):
    return n*n

squar= sqauare(7)
print(squar)

def average(*number):
    print(type(number))
    sum=0
    for i in number:
       sum =sum+i
       average= sum/len(number)
    print(average)


average(8,9,56,78,99)


def sum():
    x=8
    y=9
    print(x+y)
sum()
#Function with parameter
def my_ReverseString(x):
    return x[::-1]

mytext= 'Hippo lala'
print(my_ReverseString(mytext))

#Function with parameter # 
def sumTwoDigit(x, y):
 return int(x)+int(y)

print(sumTwoDigit('48', 66))

print(99, 'Kabir',00, -0)

#College wala # 
def sumOneToN(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
        #print(sum)
    return sum
        
#call the Function #

print(sumOneToN(10))        
        
