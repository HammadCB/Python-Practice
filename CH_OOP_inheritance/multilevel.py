class Employee:
    a=1

class Programmer(Employee): 
    b=2

class Freelancer(Programmer):
    c=3

o=Employee()
print(o.a)
# print(o.b) # Error
p=Programmer()
print(p.a)
print(p.b)
# print(p.c) # Error
q=Freelancer()
print(q.a)
print(q.b)
print(q.c)