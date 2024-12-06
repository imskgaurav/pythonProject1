#check palindrome 

list = ["m", "a", "d" ,"a", "m"]
print(list)

copy_list= list.copy()
copy_list.reverse()
print(copy_list)
if list==copy_list:
    print("PALINDROME")
else:
    print("Not Palindrome")
       
#String palaindrome 

def isPalindrome(s):
    return s==s[::-1]

str ='malayalam'
x = isPalindrome(str)
if x: 
    print('Palindrome')
else:
    print("No")    



    