import random
import time

def get_player_choice():
    # Prompt the player to enter their choice
    print("Enter your choice (rock, paper, scissors):")
    choice = input().lower()
    return choice

def is_valid_choice(choice):
    # Check if the player's choice is valid
    return choice in ['rock', 'paper', 'scissors']

def generate_computer_choice():
    # Generate a random choice for the computer
    return random.choice(['rock', 'paper', 'scissors'])

def determine_outcome(player_choice, computer_choice):
    # Determine the outcome of the game
    if player_choice == computer_choice:
        return "No winner. It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

# Main function to play the game
def main():
    while True:
        
        # Get player's choice
        player_choice = get_player_choice()
        
        # Check for valid input
        while not is_valid_choice(player_choice):
            print("Invalid input! Please enter rock, paper, or scissors.")
            player_choice = get_player_choice()
        
        # Generate computer's choice
        computer_choice = generate_computer_choice()
        
        # Countdown
        print("1")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("Shoot!")
        
        time.sleep(0.5)
        
        # Display choices with short delay
        time.sleep(0.5)
        print(f"Player chose: {player_choice}")
        time.sleep(0.5)
        print(f"Computer chose: {computer_choice}")
        
        # Determine outcome and display result with short delay
        time.sleep(0.5)
        outcome = determine_outcome(player_choice, computer_choice)
        print(outcome)
        break

main()