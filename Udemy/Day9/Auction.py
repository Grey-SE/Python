import art

print(art.logo)

isRunning = True
all_bids = {}
while isRunning:
# TODO-1: Ask the user for input
    name = input("What is your name? ")
    bid_price = int(input("What is your bid? $"))
# TODO-2: Save data into dictionary {name: price}
    all_bids[name] = bid_price
# TODO-3: Whether if new bids need to be added
    if input("Are there any other bidders? Type 'yes' or 'no': ").lower() == "no":
        isRunning = False
        print("\n" * 20)
        # TODO-4: Compare bids in dictionary
        for key, value in all_bids.items():
            if value == max(all_bids.values()):
                winner = key
                winning_bid = value
                print(f"The winner is {winner} with a bid of ${winning_bid}.")
    else:
        print("\n" * 20)
        continue


