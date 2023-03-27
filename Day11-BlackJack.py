import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def sum_of_hand(hand):
    total1 = 0
    total2 = 0
    for i in hand:
        if i != 'A':
            total1 += i
            total2 += i
        else:
            total1 += 1
            total2 += 11
    if total2 <= 21:
        return total2
    else:
        return total1


if __name__ == "__main__":
    play_in = input("Would you like to play BlackJack? Y for yes and N for No : ")
    if play_in.upper() == "Y":
        play = True
    else:
        play = False
    while play:
        in_game = True
        print(logo)
        player_hand = random.sample(cards, 2)
        dealer_hand = random.sample(cards, 2)
        player_sum = sum_of_hand(player_hand)
        print(f"Your hand : {player_hand}")
        print(f"Dealer hand : {dealer_hand[0]}")

        if player_sum == 21:
            in_game = False
            print("You got a BlackJack, You win!")
        else:
            action = input("What would you like to do? 'H' for Hit, 'S' for Stand : ")
            if action.upper() == 'H':
                deal = True
            else:
                deal = False
            while deal:
                new_card = random.choice(cards)
                player_hand.append(new_card)
                print(f"Your hand : {player_hand}")
                player_sum = sum_of_hand(player_hand)
                if player_sum > 21:
                    in_game = False
                    deal = False
                    print("You went over 21! You lose")
                else:
                    in_game = True
                    action = input("What would you like to do? 'H' for Hit, 'S' for Stand : ")
                    if action.upper() == 'H':
                        deal = True
                    else:
                        deal = False
            if in_game:
                print(f"Your hand : {player_hand}")
                print(f"Dealer hand : {dealer_hand}")
                player_sum = sum_of_hand(player_hand)
                dealer_sum = sum_of_hand(dealer_hand)
                while dealer_sum < 17:
                    new_card = random.choice(cards)
                    dealer_hand.append(new_card)
                    print(f"Dealer hand : {dealer_hand}")
                    dealer_sum = sum_of_hand(dealer_hand)
                if dealer_sum <= 21:
                    if player_sum > dealer_sum:
                        print("You got a better hand than dealer, You Win!")
                    elif player_sum == dealer_sum:
                        print("The Game is a Tie")
                    else:
                        print("Dealer has a better hand than you, You lose!")
                else:
                    print("Dealer went over 21, You win!")

        play_in = input("Would you like to play BlackJack again? Y for yes and N for No : ")
        if play_in.upper() == "Y":
            play = True
        else:
            play = False

    print("Thank You")