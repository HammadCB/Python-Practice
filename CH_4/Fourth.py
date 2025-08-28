# # List 
# # List are mutable Unlike Strings 
# friends = ["Hammad","Jawad",5,3,3.45,False,"Ali"]
# print(friends[0])
# friends[0]="Grapes"
# print(friends[0])

# #List Slicing 
# print(friends[1:4])

#----List Methods---- 

Hello = ["Hammad","Jawad",5,3,3.45,False,"Ali"]
print(Hello)

#Append 

Hello.append("Apple")
print(Hello)

#Sort / Reverse 
l1 = [1,23,32,35,15,6]
l1.sort()
print(l1)
l1.reverse()
print(l1)

#Insert 

l2=[1,2,3,4,64,83]
l2.insert(3,4)
l2.insert(5,7)
print(l2)

# #Pop

print(l2.pop(3))
print(l2)

#Remove Specific input 
l2.remove(64)
print(l2)
