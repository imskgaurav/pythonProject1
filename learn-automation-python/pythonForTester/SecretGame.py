#Enter a Number , if its matches ur Secret Number . U will win .
#Max chance will be 3 . 
secret_num= 9
guess_chance=3
count =0
while count<guess_chance:
    num = int(input("Enter the number"))
    count+=1
    if num==secret_num:
        print("U win")
        break
else:
    print("Sorry , u have exhausted ur Limit")
       
        