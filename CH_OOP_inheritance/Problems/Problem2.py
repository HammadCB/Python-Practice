class Animals:
    pass

class Pets(Animals):
    
    def meow(self):
        print("Meow!")
    pass

class Dogs(Pets):
    @staticmethod
    def bark():
        print("Woof!")
    pass

d=Dogs()
d.bark()
a=Pets()
a.meow()
d.meow()
Dogs.bark()
 #If we dont want our function to depend on Instance of the class we can use static method