#Walrus Operator 
# Allows giving a vakue to a variable as part of the expression
# :=

if(n := len([1,2,3,4,5]))>3:
    print(f"List is too long ({n} elements expected <=3)")