# Factorial 

n = int(input("Enter the number : "))
product=1
for i in range (1,n+1):
    product = product *i

print(f"The Factorial of {n} is { product}")