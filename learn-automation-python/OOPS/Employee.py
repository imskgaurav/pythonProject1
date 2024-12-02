class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@sify.com'


emp1 = Employee('Test', 'Mum', 900)

print(emp1.first)
print(emp1.last)
print(emp1.pay)
print(emp1.email)

##Add Function
a = 12
b = 9
print(a + b)
print(a.__add__(b))
