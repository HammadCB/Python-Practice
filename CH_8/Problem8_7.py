l=["Hammad","Ali","Khan"]

def rem(l,word):
    if word in l:
        l.remove(word)
        return l
    else:
        return "Word not found in the list"


word=input("Enter the word you want to remove from the list: ")
print(rem(l,word))
