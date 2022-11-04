import os
from art import logo

print(logo)
#1 = name
#2 = bid
names ={}
should_end = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for namee in bidding_record:
        bid_amount = bidding_record[namee]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = namee 
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not should_end:
 def add_new_name(name, bid): 
    new_name ={}
    new_name["name"]= name
    new_name["bid"]= bid
    names[name]=bid
 add_new_name(input("What is your Name? "),int(input("What's your Bid?: $")))
 restart = input("Are there any other bidders? Type 'yes' or 'no'.\n")
 if restart == "no":
     should_end = True
     find_highest_bidder(names)
 elif restart == 'yes':
        # Clearing the Screen
         os.system('cls')
