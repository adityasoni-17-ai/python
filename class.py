##class Area:
##    def __init__(self,length,breadth):
##        self.length=length
##        self.breadth=breadth
##r1=Area("area of rectangle",5*4)
##print(r1.length,r1.breadth)


class member1:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
class employee(member1):
    def __init__(self,name,age,salary,specialization):
        super().__init__(name,age,salary)
        self.specialization=specialization
    def y (self):
        print(self.name,self.age,self.salary,self.specialization)
class manager(member1):
      def __init__(self,name,age,salary,department):
       super().__init__(name,age,salary)
       self.department=department
      def y(self):
       print(self.name,self.age,self.salary,self.department)
a=employee("aditya",19,500000,"cse")
a.y()
a2=manager("aditya",19,50000,"cloud computing")
a2.y()
