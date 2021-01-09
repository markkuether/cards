# Single Hand Stats - if you deal a single hand of cards
# from x decks, what are the chances of dealing y hand?

import cardobjects
import poker_objects
__hand = 0

# Number of times to play.
rounds = 1000
decks = 1
print()
print("*** SINGLE HAND STATS ***")
print(f"Count types of hands delt to single hand from {decks} deck of cards.")

# Set hand types for output at end.
pokerhands = {"High Card": 0, "Two Kind": 0, "Two Pair": 0, "Three Kind": 0,
              "Straight": 0, "Flush": 0, "Full House": 0, "Four Kind": 0, "Straight Flush": 0}

# Initialize variables and create objects
mypokerhand = ""
dealer = cardobjects.DealerDeck()
hand1 = cardobjects.PlayerHand()
dealer.makedeck(decks)

# Print Header and start
print(f"Dealing {rounds} rounds:")
print("========================")
print()
for trials in range(0, rounds):
    dealer.shufflecards()

   # Deal Cards
    for cards in range(0, 5):
        hand1.addcard(dealer.takecard())

    # Evaluate Hand
    pokerhand1 = poker_objects.PokerHand(hand1.getallcards())
    mypokerhand = pokerhand1.pokerhand[__hand]

    # Count hand types

    if mypokerhand != "High Card":
        pass

    if mypokerhand in pokerhands:
        pokerhands[mypokerhand] += 1
    else:
        pokerhands[mypokerhand] = 1

    # return cards back to deck
    for hands in range(0, 5):
        dealer.addcard(hand1.takecard())

# Print summary of all rounds
for item in pokerhands:
    print(f"{item:<15} {pokerhands[item]:>10} ")

print()
print("End Of Simulation")
#wait = input("Press ENTER to continue.")
