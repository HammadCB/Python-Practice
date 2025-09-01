class Employee:
    company="Microsoft"
    def show(self):
        print(f"The name is {self.company} and salary is {self.salary}")

class Programmer:
    company="Google"
    def show(self):
        print(f"The name is {self.company} and salary is {self.salary}")

    
class Programmer(Employee): # Inheritance 
        company="Google"
        def show(self):
            print(f"The name is {self.company} and salary is {self.salary}")




a = Employee()
b= Programmer()

print(a.company,b.company)