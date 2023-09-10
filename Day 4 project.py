# day 3 was done on day 2

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
def rps():
    print("ROCK PAPER SCISSORS\nYou vs Computer\nEnter 'q' to quit\n\n")
    choices =[rock, paper, scissors]
    choice_player= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    computer_choice = random.choice(choices)

    winner = {rock:scissors, paper:rock, scissors:paper}
    print(f'You choose:\n{choices[choice_player]}\nComputer choose:\n{computer_choice}')
    choice_player = choices[choice_player]
    
    if winner[choice_player] == computer_choice:
        return print('You Won')
    elif winner[computer_choice] == choice_player:
        return print('You lose')
    else:
        return print('Draw')


rps()



