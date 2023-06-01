import art
import game_data
import random

game_over = False
score = 0
print(art.logo)

while not game_over:
    if score == 0:
        a = random.choice(game_data.data)
        b = random.choice(game_data.data)
    else:
        print(f"You are right! Current Score : {score}")
        a = b
        b = random.choice(game_data.data)

    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(art.vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
    user_choice = input("Who has more followers? Type 'A' or 'B' : ")

    if a['follower_count'] > b['follower_count']:
        correct_ans = 'A'
        if correct_ans == user_choice.upper():
            score += 1
        else:
            game_over = True
    elif a['follower_count'] < b['follower_count']:
        correct_ans = 'B'
        if correct_ans == user_choice.upper():
            score += 1
        else:
            game_over = True
    else:
        score += 1

print(f"Sorry, that is wrong, Final Score = {score}")