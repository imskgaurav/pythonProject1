class Student:

    school ='KNIT'
    def __init__(self, m1, m2, m3):
       self.m1 = m1
       self.m2 = m2
       self.m3 = m3
    def avg(self):
        return  (self.m1+self.m2+self.m3)/3

    @classmethod
    def info(cls):
        return  cls.school

s1 = Student(22, 56, 78)
print(s1.avg())
print(Student.info())




