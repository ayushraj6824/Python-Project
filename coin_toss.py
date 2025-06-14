
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