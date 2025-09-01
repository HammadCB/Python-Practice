class Demo:
    a=4



o=Demo()
print(o.a)
o.a=0
print(o.a)
#Class variable remains unchanged
print(Demo.a)
# You can create instance variable with same name as class variable
# Instance variable overrides class variable for that instance only