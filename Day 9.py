import os
os.system('cls')
class Underline:
    '''Underline text using ASCII escape sequences.
       Might not work in all terminals. if terminal does not support ASCII.
    '''
    end = '\033[0m'
    start = '\033[4m'
print('Welcome to the secret aution')
bidders = {}
name = input("What is your name?:")
bid = int(input("What is your bid?: $"))
more_bids = input("Are there any other bidders? type 'yes' or 'no'\n")
bidders[f'{name}'] = bid

while more_bids == 'yes':
    os.system('cls')
    print('Welcome to the secret aution')
    name = input("What is your name?:")
    bid = int(input("What is your bid?: $"))
    bidders[f'{name}'] = bid
    more_bids = input("Are there any other bidders? type 'yes' or 'no'\n")

highest_bid = 0

for bid in bidders:
    bid_amount = bidders[bid]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        auc_win = bid    
        name = bid#'\u0332'.join(list(bid))

print(f"The winner of the auction is {Underline.start + name + Underline.end} with a bid of ${bidders[auc_win]}.")
            