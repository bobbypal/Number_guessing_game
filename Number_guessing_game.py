import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking a number between 1 and 100.")
bot_guess = random.randint(1,100)
#print(bot_guess)
choose = input("Choose a Difficulty. type 'easy' or 'hard': ").lower()

if choose == "easy":
    attempt = 10
    while attempt > 0:
        print(f"You have {attempt} remaining to guess the answer ")
        guess = int(input("Make a guess: "))
        if guess == bot_guess:
            print("Congratulation YOU WIN ! -----You guessed the right answer")
            break
        else:
            if guess > bot_guess:
                print("Too High")
                attempt -= 1
                if attempt == 0:
                    print("YOU LOOSE")

            else:
                print("too Low")
                attempt -= 1
                if attempt == 0:
                    print("YOU LOOSE")




elif choose == "hard":
    attempt = 5
    while attempt > 0:
        print(f"You have {attempt} remaining to guess the answer ")
        guess = int(input("Make a guess: "))
        if guess == bot_guess:
            print("Congratulation YOU WIN ! -----You guessed the right answer")
            break
        else:
            if guess > bot_guess:
                print("Too High")
                attempt -= 1
                if attempt == 0:
                    print("YOU LOOSE")

            else:
                print("too Low")
                attempt -= 1
                if attempt == 0:
                    print("YOU LOOSE")



else:
    print("Invalid input")


