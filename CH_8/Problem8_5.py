def pattern(n):
    if (n==0):
        return 1
    else:
        print("*" * n)
        pattern(n-1)


pattern(6)