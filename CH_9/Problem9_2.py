# Hi score updating program
import random

def game():
    print("Welcome to the game")
    score = random.randint(1, 50)

    #Fetching high score
    with open("CH_9/HighScore.txt") as f:
        highscore = (f.read())

    if highscore != "":
        highscore = int(highscore)
    else:
        highscore = 0

#Updating high score
    print(f"Your score is {score} and high score is {highscore}")
    with open("CH_9/HighScore.txt", "w") as f:
      f.write(str(score))
      return score
game()