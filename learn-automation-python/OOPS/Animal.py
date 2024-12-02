class Animal:
    def eat(self):
     print("Animal can Eat")
      
     
    def sleep(self):
     print("Animal can sleep")
     
#Derived class 
class Cat(Animal):
     def meow(self):
         print("I can meow")
         
#Create Object of Cat class 
c = Cat()
c.eat()
c.sleep()       
c.meow()

#Create object of child class and Give reference to Parent class
a= Animal()
a.eat()
a.sleep()