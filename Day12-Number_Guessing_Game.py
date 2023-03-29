import random

logo = """

  _______  __    __   _______     _______.     _______.   .___________. __    __   _______    .__   __.  __    __  .___  ___. .______    _______ .______      
 /  _____||  |  |  | |   ____|   /       |    /       |   |           ||  |  |  | |   ____|   |  \ |  | |  |  |  | |   \/   | |   _  \  |   ____||   _  \     
|  |  __  |  |  |  | |  |__     |   (----`   |   (----`   `---|  |----`|  |__|  | |  |__      |   \|  | |  |  |  | |  \  /  | |  |_)  | |  |__   |  |_)  |    
|  | |_ | |  |  |  | |   __|     \   \        \   \           |  |     |   __   | |   __|     |  . `  | |  |  |  | |  |\/|  | |   _  <  |   __|  |      /     
|  |__| | |  `--'  | |  |____.----)   |   .----)   |          |  |     |  |  |  | |  |____    |  |\   | |  `--'  | |  |  |  | |  |_)  | |  |____ |  |\  \----.
 \______|  \______/  |_______|_______/    |_______/           |__|     |__|  |__| |_______|   |__| \__|  \______/  |__|  |__| |______/  |_______|| _| `._____|
                                                                                                                                                              

"""

if __name__ == "__main__":
    print(logo)
    print("Welcome to the Number Guessing Game")
    number = random.randint(1,100)
    print("I have a number from 1 to 100")
    difficulty = input("Choose difficulty. Type 'easy' or 'hard' : ")
    if difficulty.lower() == "easy":
        guesses = 10
    elif difficulty.lower() == "hard":
        guesses = 5
    else:
        guesses = 0
    for i in range(guesses):
        print(f"You have {guesses-i} attempts left")
        num_guess = int(input("Make a guess : "))
        if num_guess > number:
            print("Too High!")
        elif num_guess < number:
            print("Too Low!")
        else:
            print("You guessed it correctly, Well done.")
            break
        if i == guesses - 1:
            print(f"You are out of guesses! You lost, The actual number is {number}")
    print("Thanks for playing!")