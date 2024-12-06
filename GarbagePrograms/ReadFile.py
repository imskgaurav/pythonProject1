#Read txtFile#

try:
    with open('/Users/07.gaurav/PycharmProjects/pythonProject1/text.txt') as File:
         print(File.read())
except FileNotFoundError:
       print("No file Exist")         
       
#clear
# print(File.close())    