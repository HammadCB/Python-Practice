words = ["Donkey","Bad","Stupid"]

with open("CH_9/Problem4.txt") as f:
    content = f.read()
    for word in words:
        content = content.replace(word, "#"*len(word))

with open("CH_9/Problem4.txt", "w") as f:
    f.write(content)
    print("Done successfully")