import random
def Number_guessing_game(a, b):
    r1 = random.randint(a, b)
    while True:
        r2 = int(input("Guess a random number between {} and {}: ".format(a, b)))
        if r2 == r1:
            print("Well done! You guessed right.")
            break
        elif r2 > r1:
            print("You guessed too high!")
        else:
            print("You guessed too low!")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        Number_guessing_game()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    guess_number()
