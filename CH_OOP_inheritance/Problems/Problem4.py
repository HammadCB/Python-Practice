class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i


    def __add__(self,c2):
        return Complex(self.r+c2.r,self.i+c2.i)
# So Str function is Converting the output memory object into values 
# Not the c1 self values 
    def __str__(self):
        return f"{self.r}i+{self.i}j"

c1= Complex(1,3)
c2= Complex(3,8)
print(c1 + c2)    