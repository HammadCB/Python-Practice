class Employee:
    company="Microsoft"
    def show(self):
        print(f"The name is {self.company} ")

class Programmer:
    company="Google"
    def show(self):
        print(f"The name is {self.company} ")

    
class Programmer(Employee): # Inheritance 
        company="Google"
        def show(self):
            print(f"The name is {self.company} ")




a = Employee()
b= Programmer()

print(a.company,b.company)