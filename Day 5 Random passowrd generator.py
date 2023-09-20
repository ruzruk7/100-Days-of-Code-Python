import random
def password_gen():
    letters = list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
    characters = list('`~!@#$%^&*()_+-=') 
    numbers = list('1234567890')
    length = int(input("How many long do you want your password to be?\n"))
    numb_amount = int(input('How many numbers do you want in your password\n'))
    spec_char_amount = int(input("How special characters do you want in your passowrd\n"))
    password = ''
    for i in range(length+1):
        password +=random.choice(letters)
    for i in range(numb_amount+1):
        password += random.choice(numbers)
    for i in range(spec_char_amount+1):
        password += random.choice(characters)
    password = list(password)
    random.shuffle(password)
    print(f"Your password is: {''.join(password)}")


    



password_gen()
