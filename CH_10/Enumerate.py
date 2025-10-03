l=[3,5,7,234,2326,63]

index =0
for item in l:
    print(f"index is {index } : and item is {item}")
    index+=1

    #This can be simplified using enumerate function 

for index,item in enumerate(l):
    print(f"index is {index } : and item is {item}")