from os import system
from time import sleep

auction_bids = {}

def clear():
    if name=='nt':
        _ = system('cls')
    else:
        _ = system('clear')


while 1:
    name = input("Enter your name : ")
    bid = int(input("Enter your bid : $"))
    auction_bids[name] = bid
    looping = input("Are there any other bidders? Type 'yes' or 'no' : ")
    if looping.lower() == 'no':
        break
max_bid = 0
max_key = 0
for key in auction_bids:
    if auction_bids[key] > max_bid:
        max_bid = auction_bids[key]
        max_key = key
print(f"The winner of the auction is {max_key} with a bid of ${max_bid}")