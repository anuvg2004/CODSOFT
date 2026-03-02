import random

print("===== ROCK PAPER SCISSORS GAME =====")

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

while True:
    
    user_choice = input("\nChoose rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(choices)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win this round!")
        user_score += 1

    else:
        print("Computer wins this round!")
        computer_score += 1

    print("\nScore:")
    print("You:", user_score)
    print("Computer:", computer_score)

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("\nFinal Score:")
        print("You:", user_score)
        print("Computer:", computer_score)
        print("Game Over. Thanks for playing!")
        break