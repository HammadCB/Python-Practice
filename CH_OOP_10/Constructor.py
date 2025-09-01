class Employee: 
    language = "Python"
    salary = 50000

    def __init__(self,name,salary,language): #Dunder method/Constructor Starts with __ and ends with __
        #Automatically called when an object is created
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object")
        print(f"The Name is {self.name} The language is {self.language} and salary is {self.salary}")


# IF ANY OBJECT IS CREATED THEN __init__ METHOD WILL BE AUTOMATICALLY CALLED
Hammad=Employee("Hammad",50000,"Python") 

