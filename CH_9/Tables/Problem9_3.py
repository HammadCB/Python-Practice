
def generateTable(n):
    table =""
    for i in range(1,11):
        table += f"{n} x {i} = {n*i}\n"
    
    with open(f"CH_9/Tables/Table.txt{n}","w")as f:
        f.write(table)


for i in range(2,21):
    generateTable(i)