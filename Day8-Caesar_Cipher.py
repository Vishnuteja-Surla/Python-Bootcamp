def encrypt(alphabet,message, shift):
    encrypted_message = ""
    for i in message:
        encrypted_message += alphabet[(alphabet.index(i)+shift)%26]
    print(f"The encrypted message is {encrypted_message}")

def decrypt(alphabet, message, shift):
    decrypted_message = ""
    for i in message:
        decrypted_message += alphabet[(alphabet.index(i)-shift)%26]
    print(f"The decrypted message is {decrypted_message}")

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
while 1:
    operation = input("Would you like to encode a message or decode a message? : ").lower()
    message = input("Enter the message : ").lower()
    shift = int(input("Enter the shift of the code : "))
    if operation == 'encode':
        encrypt(alphabet,message,shift)
    if operation == 'decode':
        decrypt(alphabet,message,shift)
    exit_control = input("Type 'end' to stop the program and anything else continues the program : ").lower()
    if exit_control == 'end':
        break