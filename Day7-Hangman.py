import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


words_list = ['naruto','luffy','ichigo','goku','light','lelouch']
chosen_word = random.choice(words_list)
no_of_blanks = len(chosen_word)
answer_list = ['_']*no_of_blanks
print(answer_list)
lives = 6
while 1:
    guess_letter = input("Guess a Letter : ").lower()
    letter_pos = -1
    if guess_letter in answer_list:
        print('You already guessed this letter!')
    for letter in chosen_word:
        letter_pos += 1
        if letter == guess_letter:
            answer_list[letter_pos] = guess_letter
    if guess_letter not in chosen_word:
        print('Oops! Wrong Guess')
        lives -= 1
    print(answer_list)
    print(stages[lives])
    if '_' not in answer_list:
        print('You Win!')
        break
    if lives == 0:
        print("You Lose!")
        break