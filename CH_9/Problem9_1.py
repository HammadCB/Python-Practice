with open("CH_9/Problem.txt") as f:
    content = f.read()
    if "Twinkle" in content:
        print("Twinkle is present")
    else:
        print("Not Present")
