keys= ['Navin', 'Shashi', 'Harsh']
values= ['Python', 'JAVA', 'c#']
#Create Dictinory from above list 
dict1=zip(keys, values)
print(type(dict1))
dict2= dict(zip(keys, values))
print(type(dict2))
#Use get Function now #
print(dict2.get(3))
print(dict2[3])


 