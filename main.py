import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("Welcome to Guess the Number!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == number:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            return True
        elif guess < number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
        
        print(f"Attempts left: {max_attempts - attempts}")

    print(f"Sorry, you've run out of attempts. The number was {number}.")
    return False

def main():
    score = 0
    rounds = 3

    for round in range(1, rounds + 1):
        print(f"\nRound {round}")
        if play_game():
            score += 1

    print(f"\nGame over! Your final score is {score}/{rounds}")

if __name__ == "__main__":
    main()
