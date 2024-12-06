import json
from math import e
emp = {}
print(type(emp))
emp = {"pawan" : 3000, "Ramesh" : 4000}
print(emp)
#Convert dictionary into json//
json1 = json.dumps(emp, indent=2)
print(type(json1))
print(json1)

##Create new dictionary and play with DICTINAORY Functions

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 1999
}
print(thisdict)
x = thisdict["brand"]
print(x)
year= thisdict["year"]
print(year)

# get method is also to find the value against key#
key1= thisdict.get("brand")
print(key1)
#Get a list of the keys:
keysVal = thisdict.keys()
print(keysVal)
#Get a list of the values:
values = thisdict.values()
print(values)
#Change item in Dictionary 
thisdict["model"] = "Ford Endeavour"
print(thisdict)
#Add items 
thisdict["color"] = 'RED'
print(thisdict)
thisdict["Fuel"] = 'PETROL'
print(thisdict)
thisdict.popitem()
print(thisdict)

#Print all key names in the dictionary, one by one:#

for x in thisdict:
    print(x)
    
#print All values of dictinary 
print('All Values are :+')
for x in thisdict:
    print(thisdict[x])
    
# 	Returns a list containing a tuple for each key value pair
print(thisdict.items())    