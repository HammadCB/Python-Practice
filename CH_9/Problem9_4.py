word = "Donkey"

with open("CH_9/Problem4.txt") as f:
    content = f.read()
    content = content.replace(word, "#######")

with open("CH_9/Problem4.txt", "w") as f:
    f.write(content)
    print("Done successfully")