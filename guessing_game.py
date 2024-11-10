import random

def welcome():

    print("Welcome to Noir's guessing game")
    print("I'm thinking of a number between 1 - 100\n")

    difficulty()


def difficulty():
    chances = 0

    print("Please select a difficulty: \n")
    print("1.Easy (10 chances)")
    print("2.Medium (5 chances)")
    print("3.Hard (3 chances)\n")

    choice = input("Enter your choice: ").lower()

    if choice == "1" or choice == "one":
        chances += 10
        print("Great! You have selected the Easy difficulty level.")
    elif choice == "2" or choice == "two":
        chances += 5
        print("Great! You have selected the Medium difficulty level.")
    elif choice == "3" or choice == "three":
        chances += 3
        print("Great! You have selected the Hard difficulty level.")


    print("Lets start the game!!!")

    game(chances)


def game(chances):
    noir_num = random.randint(1,10)
    attempts = 0
    

    while chances > 0:
        guess = int(input("Enter your guess: "))
        attempts += 1
        chances -= 1

        if guess > noir_num:
            print("Incorrect! The number is less than", guess)
        elif guess < noir_num:
            print("Incorrect! The number is greater than", guess)
        else:
            print("Congrats! You win. It took", attempts, "tries.")
            return  # Exit the game function if the user wins

    print("Out of chances! The number was", noir_num)
        

def main():

    while True:
        welcome()
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for playing!")
            break

main()
