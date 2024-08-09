import random

def display_instructions():
    instructions = """
    Welcome to the Rock-Paper-Scissors Game!
    Instructions:
    1. Choose one of the following options:
       'r' for Rock
       'p' for Paper
       's' for Scissors
    2. The computer will also make a choice.
    3. The winner is determined by the following rules:
       - Rock (r) beats Scissors (s)
       - Scissors (s) beat Paper (p)
       - Paper (p) beats Rock (r)
    4. If both choices are the same, it's a draw.
    5. Scores are tracked and displayed after each round.
    6. You can play multiple rounds and see the final scores at the end.
    \n\t Let's start the game!\n
    """
    print(instructions)

def get_computer_choice():
    choices = ["r", "p", "s"]
    return random.choice(choices)

def determine_winner(you, computer):
    if you == computer:
        return "It's a draw!"
    elif (you == "r" and computer == "s") or \
         (you == "s" and computer == "p") or \
         (you == "p" and computer == "r"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    display_instructions()
    
    user_score = 0
    computer_score = 0

    choice_dict = {"r": "Rock", "p": "Paper", "s": "Scissors"}

    while True:
        youstr = input("Enter your choice (r/p/s): ").lower()

        if youstr not in choice_dict:
            print("Invalid choice! Please choose 'r' for Rock, 'p' for Paper, or 's' for Scissors.\n")
            continue

        you = youstr
        computer = get_computer_choice()

        print(f"\nYou chose: {choice_dict[you]}")
        print(f"Computer chose: {choice_dict[computer]}\n")

        result = determine_winner(you, computer)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"Scores -> You: {user_score}, Computer: {computer_score}\n")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("\nFinal Scores")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
