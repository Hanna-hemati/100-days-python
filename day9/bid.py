print("HI, program started!")

dic = {}
def highest_bidder(bidding_continue):
    highest_bid = 0
    for bidder in bidding_continue:
        bid_amount = bidding_continue[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"the winner is {winner} with bid of ${highest_bid}")


continue_biding = True
while continue_biding:
    name = input("what is your name?")
    bid_price = int(input("what is your bid? $"))
    dic[name] = bid_price
    should_continue = input("are there any bidders? type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        continue_biding = False
        highest_bidder(dic)
    elif should_continue == "yes":
        print("\n" * 10)


