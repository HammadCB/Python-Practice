#Capable of Square cube and square root
class calculator:
    def __init__(self,number):
        self.number=number
    def square(self):
        return self.number**2
    def cube(self):
        return self.number**3
    def squareroot(self):
        return self.number**0.5
a=calculator(9)
print("welcome to calculator")
print(a.square())
print(a.cube())
print(a.squareroot())
