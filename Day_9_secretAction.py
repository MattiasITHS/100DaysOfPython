from replit import clear
# HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("Welcome to the secret auction program")

bids = {}


def find_higest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # EX, bidding_record{"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winnder = bidder
    print(f"The winner is {winner} with a bid of ${higest_bid}")


bidding_finished = False
while not more_bidders:
    name = input("What is your name?: ")
    price = int(input("Whats is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if should_continue == 'no':
        bidding_finished = True
        find_higest_bidder(bids)
    elif should_continue == 'yes':
        clear()

# bids = {}
# bidder = []
# def secret_auction():
#   other_bidders = True
#   while other_bidders:
#     name = input("What is your name? ")
#     bids["name"] = name
#     bid_amount = input("What is your bid? $")
#     bids["amount"] = bid_amount
#     bidder.append(bids)
#     bidders = input("Are there any other bidders? Type 'yes' or 'no'")
#     if bidders == 'no':
#       other_bidders = False
#     else:
#       clear()
#   bidder.sorted()


# secret_auction()
# print(bidder)