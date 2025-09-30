import random
import os
import time

# Color codes for better UI
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print(f"{Colors.CYAN}{Colors.BOLD}")
    print("🎯" + "="*50 + "🎯")
    print("        WELCOME TO THE ULTIMATE GUESSING GAME!")
    print("🎯" + "="*50 + "🎯")
    print(f"{Colors.END}")

def get_difficulty():
    print(f"\n{Colors.YELLOW}Choose your difficulty level:{Colors.END}")
    print(f"{Colors.BLUE}1. Easy (1-50) - 10 points per guess{Colors.END}")
    print(f"{Colors.YELLOW}2. Medium (1-100) - 5 points per guess{Colors.END}")
    print(f"{Colors.RED}3. Hard (1-200) - 2 points per guess{Colors.END}")
    print(f"{Colors.PURPLE}4. Expert (1-500) - 1 point per guess{Colors.END}")
    
    while True:
        try:
            choice = int(input(f"\n{Colors.CYAN}Enter your choice (1-4): {Colors.END}"))
            if choice in [1, 2, 3, 4]:
                difficulties = {
                    1: ("Easy", 1, 50, 10),
                    2: ("Medium", 1, 100, 5),
                    3: ("Hard", 1, 200, 2),
                    4: ("Expert", 1, 500, 1)
                }
                return difficulties[choice]
            else:
                print(f"{Colors.RED}Please enter a number between 1 and 4!{Colors.END}")
        except ValueError:
            print(f"{Colors.RED}Please enter a valid number!{Colors.END}")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_hint(number, guess, difficulty_name):
    hints = []
    
    # Distance hint
    distance = abs(number - guess)
    if distance <= 5:
        hints.append(f"{Colors.RED}🔥 VERY HOT!{Colors.END}")
    elif distance <= 10:
        hints.append(f"{Colors.YELLOW}🌡️ Hot{Colors.END}")
    elif distance <= 20:
        hints.append(f"{Colors.BLUE}❄️ Cold{Colors.END}")
    else:
        hints.append(f"{Colors.CYAN}🧊 VERY COLD!{Colors.END}")
    
    # Even/Odd hint
    if number % 2 == 0:
        hints.append(f"{Colors.GREEN}💡 Hint: The number is even{Colors.END}")
    else:
        hints.append(f"{Colors.GREEN}💡 Hint: The number is odd{Colors.END}")
    
    # Prime hint
    if is_prime(number):
        hints.append(f"{Colors.PURPLE}🔢 Hint: The number is prime{Colors.END}")
    else:
        hints.append(f"{Colors.PURPLE}🔢 Hint: The number is composite{Colors.END}")
    
    # Range hint
    if guess < number:
        hints.append(f"{Colors.YELLOW}📈 Higher!{Colors.END}")
    else:
        hints.append(f"{Colors.BLUE}📉 Lower!{Colors.END}")
    
    return hints

def calculate_score(guesses, max_guesses, points_per_guess, difficulty_name):
    base_score = max(0, (max_guesses - guesses + 1) * points_per_guess)
    bonus = 0
    
    if guesses <= 3:
        bonus = 50
    elif guesses <= 5:
        bonus = 25
    elif guesses <= 7:
        bonus = 10
    
    total_score = base_score + bonus
    return total_score, bonus

def play_game():
    clear_screen()
    print_banner()
    
    difficulty_name, min_num, max_num, points_per_guess = get_difficulty()
    number = random.randint(min_num, max_num)
    max_guesses = (max_num - min_num) // 10 + 5  # Adaptive max guesses
    guesses = 0
    score = 0
    
    print(f"\n{Colors.GREEN}🎮 Starting {difficulty_name} mode!")
    print(f"🎯 Guess a number between {min_num} and {max_num}")
    print(f"🏆 You have {max_guesses} guesses maximum")
    print(f"💎 Earn {points_per_guess} points per remaining guess!{Colors.END}")
    
    while guesses < max_guesses:
        guesses += 1
        remaining = max_guesses - guesses + 1
        
        print(f"\n{Colors.CYAN}{'='*50}")
        print(f"Guess #{guesses} | Remaining: {remaining} | Current Score: {score}")
        print(f"{'='*50}{Colors.END}")
        
        while True:
            try:
                guess = int(input(f"\n{Colors.WHITE}Enter your guess: {Colors.END}"))
                if min_num <= guess <= max_num:
                    break
                else:
                    print(f"{Colors.RED}Please enter a number between {min_num} and {max_num}!{Colors.END}")
            except ValueError:
                print(f"{Colors.RED}Please enter a valid number!{Colors.END}")
        
        if guess == number:
            score, bonus = calculate_score(guesses, max_guesses, points_per_guess, difficulty_name)
            
            print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 CONGRATULATIONS! 🎉{Colors.END}")
            print(f"{Colors.GREEN}You guessed it right in {guesses} guesses!")
            print(f"🎯 The number was: {number}")
            print(f"🏆 Your score: {score} points")
            if bonus > 0:
                print(f"✨ Bonus points: {bonus}")
            
            # Performance message
            if guesses <= 3:
                print(f"{Colors.YELLOW}🌟 AMAZING! You're a guessing master!{Colors.END}")
            elif guesses <= 5:
                print(f"{Colors.BLUE}👏 Great job! Excellent guessing!{Colors.END}")
            elif guesses <= 7:
                print(f"{Colors.GREEN}👍 Well done! Good guessing!{Colors.END}")
            else:
                print(f"{Colors.CYAN}💪 Nice work! You got it!{Colors.END}")
            
            return score, guesses, True
        else:
            hints = get_hint(number, guess, difficulty_name)
            for hint in hints:
                print(hint)
            
            # Update score
            score = max(0, (max_guesses - guesses) * points_per_guess)
    
    print(f"\n{Colors.RED}{Colors.BOLD}💀 GAME OVER! 💀{Colors.END}")
    print(f"{Colors.RED}You ran out of guesses!")
    print(f"🎯 The number was: {number}")
    print(f"🏆 Final score: {score} points")
    print(f"{Colors.YELLOW}Better luck next time!{Colors.END}")
    
    return score, guesses, False

def main():
    total_games = 0
    total_score = 0
    best_score = 0
    best_guesses = float('inf')
    
    while True:
        score, guesses, won = play_game()
        
        total_games += 1
        total_score += score
        best_score = max(best_score, score)
        if won:
            best_guesses = min(best_guesses, guesses)
        
        print(f"\n{Colors.CYAN}{'='*50}")
        print(f"📊 GAME STATISTICS")
        print(f"{'='*50}")
        print(f"🎮 Games played: {total_games}")
        print(f"🏆 Total score: {total_score}")
        print(f"⭐ Best score: {best_score}")
        if best_guesses != float('inf'):
            print(f"🎯 Best performance: {best_guesses} guesses")
        print(f"📈 Average score: {total_score // total_games}")
        print(f"{'='*50}{Colors.END}")
        
        while True:
            play_again = input(f"\n{Colors.YELLOW}Would you like to play again? (y/n): {Colors.END}").lower()
            if play_again in ['y', 'yes', 'n', 'no']:
                break
            print(f"{Colors.RED}Please enter 'y' or 'n'!{Colors.END}")
        
        if play_again in ['n', 'no']:
            print(f"\n{Colors.GREEN}Thanks for playing! See you next time! 👋{Colors.END}")
            break
        
        clear_screen()

if __name__ == "__main__":
    main()
    