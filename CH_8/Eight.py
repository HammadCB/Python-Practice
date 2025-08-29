# # Functions 

# a = int(input("Enter your number :"))
# b = int(input("Enter your number :"))
# c = int(input("Enter your number :"))
# average = (a+b+c)/3
# print(average)

# # Instead of doing this again and again Create Function


# def avg():
#      a = int(input("Enter your number :"))
#      b = int(input("Enter your number :"))
#      c = int(input("Enter your number :"))
#      average = (a+b+c)/3
#      print(average)

# avg()
# avg()


# #Arguement 

# name = (input("What is you name : "))

# def NAME(name):
#      print("Good morning : ", name)

# NAME(name)



# # USER DEFINED FUNCTIONS
# # BUILT IN FUNCTIONS 

# #Arguement

# alpha = (input("What is you name : "))

# def Bravo(alpha):
#      print("Good morning : ", alpha)
#      return  3
# # RETURN if we want to take value from the function and Put it in Variable out side 
# a=Bravo(alpha)
# print(a)

# b=Bravo(alpha)
# print(b)

# c=a+b
# print(c)


#If we do not give value we have to give Default Value otherwise Error
def goodDay(name,ending="Thankyou"):
            print(f"Good Day, {name}")

            print(ending)


goodDay("Hammad")
goodDay("Hammad","Weirdo")








