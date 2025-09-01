class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary,pin):
        self.name = name
        self.pin = pin
        self.salary = salary


p=Programmer("Hammad", 100000,1234)
print(p.name, p.salary, p.pin, p.company)
q=Programmer("Raif", 50000,1235)
print(q.name, q.salary, q.pin, q.company)
