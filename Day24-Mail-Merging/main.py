# Constants
STARTING_LETTER_PATH = "./Input/Letters/starting_letter.txt"
INVITED_NAMES_PATH = "./Input/Names/invited_names.txt"
READY_TO_SEND_FOLDER = "./Output/ReadyToSend/"

with open(INVITED_NAMES_PATH, mode="r") as names_file:
    names = names_file.readlines()
with open(STARTING_LETTER_PATH, mode="r") as starting_text_file:
    start_letter = starting_text_file.read()
for i in names:
    i = i.strip('\n')
    with open(READY_TO_SEND_FOLDER + f"letter_to_{i}.txt", mode="w") as letter:
        letter.write(start_letter.replace("[name]", i))
