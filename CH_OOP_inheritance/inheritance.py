class Employee:
    company="Microsoft"
    def show(self):
        print(f"The name is {self.name} and salary is {self.salary}")

class Programmer:
    company="Google"
    def show(self):
        print(f"The name is {self.name} and salary is {self.salary}")

    def showlanguage(self):
        print(f"The name is {self.name} and language is {self.language}")

    
class Programmer(Employee): # Inheritance 
        company="Google"
        def show(self):
            print(f"The name is {self.name} and salary is {self.salary}")

        def showlanguage(self):
            print(f"The name is {self.name} and language is {self.language}")


a = Employee()
b= Programmer()

print(a.company,b.company)