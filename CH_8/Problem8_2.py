# Celcius To Fahrenheit
def F_to_C(f):
    return  5*(f-32)/9
    

f=int(input("Enter temperature in Fahrenheit: "))
print("Temperature in Celcius is: ",round(F_to_C(f)),"°C")

# Round for making the Return Value More Readable