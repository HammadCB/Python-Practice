import random
n = random.randint(1,100)
a=-1
guesses = 0
while (a !=n):
    guesses +=1
    a = int (input("Guess the number between 1 to 100:"))
    if(a>n):
        print("Lower number please ")
    elif(a<n):
        print("Higher number please")
    else:
        print("You guessed it right in",guesses,"guesses")
    