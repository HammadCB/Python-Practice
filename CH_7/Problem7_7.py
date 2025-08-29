''' STAR PATTERN
 n = 3 
     .
    ...
   ......

   
'''


# end="" Removes next line function


n= int(input("Enter the number of lines : "))

for i in range (1,n+1):# Work till n number of lines 
    print(" "* (n-i),end="") # Spaces to make it center 
    print("*"* (2*i-1),end="") #Stars 
    # Spaces Decrease Starts increase making it evenly Center 
    print("")   





