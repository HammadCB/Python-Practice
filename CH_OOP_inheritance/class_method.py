class Employee:
    a=1
    @classmethod
    def show (cls):
        print(f"This is Employee class method {cls.a}")
#CLS IF WE WANT TO ACCESS CLASS VARIABLE INSIDE CLASS METHOD WE USE CLS KEYWORD
e = Employee()
e.a =45
e.show()