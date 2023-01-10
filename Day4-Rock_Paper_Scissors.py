import random
paper = '📄'
scissors = '✂'
rock = '🗿'
choices = [rock, paper, scissors]
print("Let's play Rock, Paper, Scissors")
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
pc_choice = random.randint(0,2)
print(f"Your Choice : {choices[your_choice]}    Computer Choice : {choices[pc_choice]}")
if your_choice == pc_choice:
    print("It's a Draw")
else:
    if your_choice == 0:
        if pc_choice == 1:
            print("You Lose!")
        else:
            print("You Win!")
    elif your_choice == 1:
        if pc_choice == 2:
            print("You Lose!")
        else:
            print("You Win!")
    else:
        if pc_choice == 0:
            print("You Lose!")
        else:
            print("You Win!")