class Employee:
    salary = 50000

    def __init__(self):
        self._increment = 0.05   # private variable

    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, salary):
        # calculate increment % needed to reach target salary
        self._increment = (salary / self.salary) - 1 
        

    @property
    def salary_after_increment(self):
        return self.salary * (1 + self._increment)


e = Employee()
print(e.salary_after_increment)  # 52500.0 (because 5% increment)

e.increment = 60000              # set increment so final salary = 60000
print(e.salary_after_increment)
print(e.increment)               # 60000.0


e.increment = 90000    
print(e.salary_after_increment)
print(e.increment)             #How much incremement requited to get targeted Salary
