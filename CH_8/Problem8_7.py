l = ["Hammad", "Ali", "Khan", "Jawad"]

def rem(l, word):
    n = []
    for item in l:
        if not (item == word):
          n.append(item.strip(word))   
    return n

print(rem(l, "ad"))
