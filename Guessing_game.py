# Guessing game
import random   
def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    while True:
        user_guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        if user_guess < number_to_guess:
            print("Too low!")
        elif user_guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break   
if __name__ == "__main__":
    guessing_game() 
    