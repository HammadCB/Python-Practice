class Employee:
    a=1
    @classmethod
    def show (cls):
        print(f"This is Employee class method {cls.a}")

    @property
    def name(self):
        return (f"{self.fname} {self.lname}")
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]  #Spliting the first name and last name
        self.lname = value.split(" ")[1]  #Making it Like a list



e = Employee()
e.a = 45

e.name="Hammad Farooqi"
print(e.fname, e.lname)

e.show()
#Example of encapsulation and Abstraction