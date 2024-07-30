##class person1:
##    def __init__(self,first,last):
##        self.first=first
##        self.last=last
##    def x(self):
##        print(self.first,self.last)
##class student(person1):
##    def __init__(self,first,last,date):
##        super().__init__(first,last)
##        self.date=date
##    def y(self):
##         print(self.first,self.last,self.date)
##a=student("adity","soni",2004)
##a.y()
##

class person1:
     def __init__(self,first,age):
         self.first=first
         self.age =age
     def x(self):
         print(self.first,self.age)
class school(person1):
      def __init__(self,first,age,school):
          super().__init__(first,age)
          self.school=school
      def y(self):
           print(self.first,self.age,self.school)
a = school("aditya",19,"convent")
a.y()






    










