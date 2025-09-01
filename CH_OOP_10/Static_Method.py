class Employee: 
    language = "Python"
    salary = 50000

    def getinfo(self):#Instance method for class Employee
        print(f"The language is {self.language} and salary is {self.salary}")

    @staticmethod
    def greet():#Static Method
        #Dont need self parameter because it is not dependent on instance or class variable
        print("Hello, Welcome to the Company")

Hammad=Employee() 
Hammad.getinfo()
Hammad.greet()


