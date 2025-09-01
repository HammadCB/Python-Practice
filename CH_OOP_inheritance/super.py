class Employee:
    def __init__(self):
        print("Employee Constructor called")
    a=1

class Programmer(Employee): 
    def __init__(self):
        print("Programmer Constructor called")
    b=2

class Freelancer(Programmer):
    def __init__(self):
        super().__init__() # Calls the constructor of Programmer as it is the immediate parent class
        print("Freelancer Constructor called")
    c=3

# o=Employee()
# print(o.a)
# # print(o.b) # Error
# p=Programmer()
# print(p.a)
# print(p.b)
# # print(p.c) # Error
q=Freelancer()
print(q.a)
print(q.b)
print(q.c)