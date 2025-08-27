# String is Immutable 
# String Slicing 

name = "Hammad"

# IF we count from Left its 0 1 if Right to left we start counting from -1 -2
 # Syntax Name of variable = the variable we want to talk about [0:6][-1:-5]

nameshort = name[-6:-3] # Start from index 0 excluding all the way till 3 ( excluding 3 )
character1 =name[1:4]


print (nameshort)
print (character1)
print(name[1:3])
print(name[1:])
print(name[:5])



# Skip Value 
# Same as Slicing but we add The Starting index Ending index then the num of indexes we want to skip


word = "0123456789"
print (word [0:6:2])
