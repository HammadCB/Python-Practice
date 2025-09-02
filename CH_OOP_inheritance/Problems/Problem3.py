class Employee:
    salary=50000
    increment=0.5 
    @property
    def salary_after_increment(self):
        self.salary * self.increment 

e=Employee()
print(e.salary_after_increment)