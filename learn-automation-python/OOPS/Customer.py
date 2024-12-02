class Customer:
    def __init__(self, name, membership_type):
         self.name = name
         self.membership_type = membership_type
         
    def __str__(self):
        return self.name+ " "+ self.membership_type
    
    def __eq__(self, other):
        if self.name==other.name and self.membership_type==other.membership_type:
         return True
        
        return False
    
c = Customer("Bob", "Super")
d = Customer("Bob","Super")

#print(c)
print(c.__eq__(d))
