#Recursion 

'''Instead of Factorial (5)
With Recursion we can Divide the problem in small parts till it gets easy 
For Exampled We do'''
#n!=n*(n-1)!


def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)


n = int(input("Enter a number "))
print(f"The Factorial of this number is : {factorial(n)}")


