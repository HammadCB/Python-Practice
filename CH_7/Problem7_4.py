n = int(input("Enter a number : "))

if n <= 1:
    print("Number is not prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Number is not prime")
            break
    else:   # runs only if loop didn’t break
        print("Number is Prime")
