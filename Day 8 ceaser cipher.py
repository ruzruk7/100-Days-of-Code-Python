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
active = True
message_index = []
alphabet_index = []

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
while active:
    action = input("Type 'encode' to encrypt and 'decode' to decrypt: ").lower()
    message = input("Type your message:\n")
    ciper_number = int(input("Type the shift number"))
    if action == 'encode':
        message = list(message)
        for mes_i, mes_letter in enumerate(message):
            for i, letter in enumerate(alphabet):
                alphabet_index.append(i)# ??
                if mes_letter == letter:
                    i += ciper_number
                    if i > 25:
                        i -= 25
                    message[mes_i]= alphabet[i]
        print (f"Here is your encrypted message: {''.join(message)}")
    if action == 'decode':
        message = list(message)
        for mes_i, mes_letter in enumerate(message):
            for i, letter in enumerate(alphabet):
                alphabet_index.append(i)# ??
                if mes_letter == letter:
                    i -= ciper_number
                    if i < 0 :
                        i += 25
                    message[mes_i]= alphabet[i]
        print (f"Here is your decrypted message: {''.join(message)}")



