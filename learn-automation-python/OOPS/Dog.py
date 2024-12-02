
class Dog:
    
    
    def __init__(self,name):
        self.name= name
   
    def bark(self):
         print("Bark")
         
         
    @property
    def name(self):
        print("Setting nAME")
        return self._name
    
    @name.setter
    def set_name(self, name):
        print("Getting Name")
        self._name= name
    
    @name.getter
    def get_name(self):
       return self.name
             
         
#d = Dog("Naag")
d= Dog("Mumbai")
print(d.set_name("Test"))
print(d.name("Test"))
print(type(d))
print(d.bark())
         