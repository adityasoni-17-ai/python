##
##class triangle:
##    def __init__(self,length,width,height):
##        self.length=length
##        self.width=width
##        self.height=height
##r1=triangle("perimeter of triangle",45+50+55)
##r2=triangle("area of triangle",(1/2*50*55))
##print(r1.length,r1.width,r1.height)
##print(r2.width,r2.height)


class average:
    def __init__(self ,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
                
a = int(input("enter a"))
b = int(input("enter b"))
c = int(input("enter c"))
d=int(input("enter d"))


a1=average("find averag",a+b+c+d/4)
print(a1.a,a1.b,a1.c,a1.d)
