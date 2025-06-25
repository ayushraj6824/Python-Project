
import random
while True:
    choice = input("Do you want to toss the coin? (yes/no): ").strip().lower()
    if choice == 'yes':
        toss = random.choice(['Heads', 'Tails'])
        print(f"The coin landed on: {toss}.")
    elif choice == 'no':
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# This code simulates a coin toss game where the user can choose to toss the coin or exit the game.
# It uses the random module to randomly select between 'Heads' and 'Tails'. # The game continues until the user decides to stop by entering 'no'.
# The input is validated to ensure the user enters either 'yes' or 'no'.    