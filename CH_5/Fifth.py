#Dictionary  
 # It is unordered , Mutable ,Indexed,No duplicate keyys 
# NOTE in dictionary we use { } instead of [ ] ( )
marks = {
    "Hammad": 100,
    "Haris": 45,
    "Sam": 53,
    0 : "Ahmed "
}

# print(marks,type(marks))
# print(marks["Hammad"]) 
# print(marks[0])

#Dictionary Methods 

# print(marks.items())
# print(marks.keys())
# print(marks.values())

# #Can update Previous written and also add more like this 
# marks.update({"Hammad":99,"Mike":33})
# print(marks["Hammad"])
# print(marks.items())

#Get Method 

# print(marks.get("Ali"))
print(marks.get("Hammad2"))
print(marks["Hammad2"])
# Difference Between them is that .get give return statement if dont found instead of error 

 