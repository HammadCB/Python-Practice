# Inches to Centimeters conversion table

def in_to_cm(inch):
    cm = inch * 2.54
    return cm

print("Inches\tCentimeters")
print("---------------------")
a=input("Enter the number of inches you want to convert to centimeters: ")
print(in_to_cm(3))