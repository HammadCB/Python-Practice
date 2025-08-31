import random
import time
from colorama import Fore, Style


# Function to display welcome message

def display_welcome_message():  
    print(Fore.GREEN + "Welcome to Snake Water Gun Game" + Style.RESET_ALL)
    time.sleep(1)
    print(Fore.YELLOW + "You will be playing against the computer" + Style.RESET_ALL)
    time.sleep(1)
    print("You will have 10 chances to play")
    time.sleep(1)
    print("All the best!")
    time.sleep(1)

# Function to print the result of each round

def print_round_result(player_choice, computer_choice, winner):
    print(f"Your guess: {player_choice}, Computer's guess: {computer_choice}")
    if winner == "player":
        print(Fore.GREEN + "You win 1 point" + Style.RESET_ALL)
    elif winner == "computer":
        print(Fore.RED + "Computer wins 1 point" + Style.RESET_ALL)
    else:
        print("It's a tie!")

#Basic Rules
 
def play_game():
    chance = 10
    no_of_chance = 0
    player_point = 0
    computer_point = 0
    game_list = ["snake", "water", "gun"]
    rules = {"snake": "water", "water": "gun", "gun": "snake"}

#Game Start Stop condition

    while no_of_chance < chance:
        while True:
            _input = input("Snake, Water, Gun: ").lower()
            #Valid input Break it and Continue Rest of conditions 
          
            if _input in game_list:
                break
            print("Invalid input! Please choose from Snake, Water, or Gun.")
          #for invalid input check this condition then get out of the loop and jumps to the next iteration of the outer loop
        _random = random.choice(game_list)

        #GAME RULES 
        if _input == _random:  # Checkes input = random
            print_round_result(_input, _random, "tie")
        elif rules[_input] == _random: # Takes input as key and checks value with random if random has correct value player wins  wins
            player_point += 1
            print_round_result(_input, _random, "player")
        else:
            computer_point += 1 # Takes input as key and checks value with random if random has wrong  value 
                                #It already checked for tie and player did not match the fixed rules   so computer wins as it didnt trigger at other functions 
            print_round_result(_input, _random, "computer")
        
        no_of_chance += 1
        print(f"{chance - no_of_chance} chances left out of {chance}") # Total chances - chance used = Remaining chances
        print(f"Your points: {player_point}, Computer points: {computer_point}")
        print("\n")
    
    print("Game Over!")# When chances are over it will print game over and final result
    if player_point > computer_point:
        print(Fore.GREEN + "Congratulations! You won the game!" + Style.RESET_ALL)
    elif player_point < computer_point:
        print(Fore.RED + "Computer wins the game! Better luck next time." + Style.RESET_ALL)
    else:
        print("It's a tie!")
    print(f"Final Score: You - {player_point}, Computer - {computer_point}")

if __name__ == "__main__": # For running the game only when the script is executed directly
    display_welcome_message()
    play_game()