# '''

# a=" a very long string with emails 
# Extract from a text file
# Must store sowmething 
# emails =[]
# 3 seconds
# READ / WRITE
# Extratcting Data From Ninth.txt
# '''
#   #Must Close the file after opening it
# f=open("CH_9/Ninth.txt")
# data = f.read()
# print(data)
# f.close()

# # Two types of files
# # Text files
# # Binary files

# #READ
# #mode r, w, a, r+, rb, wb, ab, rb+


# st=" Hammad is a very Amazing  guy "
# f=open("CH_9/Ninth.txt","w")
# f.write(st)
# f.close() 

# f=open("CH_9/Ninth.txt")
# lines1 = f.readline()
# print(lines1, type(lines1))
# lines2 = f.readlines()
# print(lines2, type(lines2))
# f.close()
# #f.readline() #reads one line at a time
# #f.readlines() #reads all lines and stores in a list

# f= open("CH_9/Ninth.txt", "r")
# line = f.readline()
# while(line != ""):
#     print(line)
#     line = f.readline()

# f.close()

#Append mode
f= open("CH_9/Ninth.txt", "a")
f.write("\nSet up Github also ")
f.close()


#with statement
with open("CH_9/Ninth.txt") as f:
    data = f.read()
    print(data)
    # NO NEED TO CLOSE WITH WITH STATEMENT