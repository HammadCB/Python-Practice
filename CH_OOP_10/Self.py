class Employee: 
    language = "Python"
    salary = 50000

    def getinfo(self):#Instance method for class Employee
        print(f"The language is {self.language} and salary is {self.salary}")



Hammad=Employee() 
Hammad.language="Java" 
Hammad.getinfo()

