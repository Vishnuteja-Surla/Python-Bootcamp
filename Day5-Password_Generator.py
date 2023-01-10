import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
length_of_password = int(input("Enter the number of characters in your password : "))
password = ""
if length_of_password >= 8:
    no_of_numbers = int(input("Enter the number of Numbers you want in your password : "))
    no_of_symbols = int(input("Enter the number of symbols you want in your password : "))
    selected_letters = []
    selected_numbers = []
    selected_symbols = []
    for i in range(no_of_numbers):
        selected_numbers.append(random.choice(numbers))
    for i in range(no_of_symbols):
        selected_symbols.append(random.choice(symbols))
    for i in range(length_of_password - (no_of_numbers + no_of_symbols)):
        selected_letters.append(random.choice(letters))
    selected = selected_letters + selected_numbers + selected_symbols
    random.shuffle(selected)
    for i in selected:
        password += i
    print("Your Password is : ",password)
else:
    print("Any decent Password must have atleast 8 characters")