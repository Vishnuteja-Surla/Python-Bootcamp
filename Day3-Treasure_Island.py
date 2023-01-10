print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the Treasure Island, Luffy.")
print("Your Mission is to find the One Piece on this Raftel island")
print("You have only two paths. Where do you want to go? Type left or right.")
choice =  input()
if choice.lower() == 'left':
    print("You reached an extension of sea into the island that you must cross. Will you swim across or build a raft? Type swim or raft.")
    choice = input()
    if choice.lower() == 'swim':
        print("Man, you are a Devil Fruit Eater, you cannot swim. Hey, Davy Jones welcomes you...Game Over")
    elif choice.lower() == 'raft':
        print("Not the best raft, but works I guess")
        print("You have 3 caves infront of you and one has treasure. First one is coated red, second is blue and last is green.What do you choose? Type the color")
        choice = input()
        if choice.lower() == 'red':
            print("You entered the room of fire, severe burns and Game Over...")
        elif choice.lower() == 'blue':
            print("Something is glittering! Is that the One Piece?? Might be but is a treasure for sure")
        elif choice.lower() == 'green':
            print("You entered the room of acid, melts the rubber and Game Over...")
        else:
            print("Hey, I said to choose one colors mentioned above. Don't violate the rules.")
    else:
        print("Hey, I said to choose one between swim and raft. Don't violate the rules.")
elif choice.lower() == 'right':
    print("Oops! You ran into quick sand. Looks deep...Game Over")
else:
    print("Hey, I said to choose one between left and right. Don't violate the rules.")