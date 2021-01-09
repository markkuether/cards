# Two Hand Stats - if you deal two hands of cards
# from x decks, what are the chances of dealing y hand?

import cardobjects
import poker_objects
__hand = 0

# Number of times to play.
rounds = 1000
decks = 1
print()
print("*** TWO HAND STATS ***")
print(f"Count types of hands delt to two hands from {decks} deck of cards.")

# Set hand types for output at end
pokerhands1 = {"High Card": 0, "Two Kind": 0, "Two Pair": 0, "Three Kind": 0,
               "Straight": 0, "Flush": 0, "Full House": 0, "Four Kind": 0, "Straight Flush": 0}
pokerhands2 = {"High Card": 0, "Two Kind": 0, "Two Pair": 0, "Three Kind": 0,
               "Straight": 0, "Flush": 0, "Full House": 0, "Four Kind": 0, "Straight Flush": 0}

# Initialize variables and create objects
mypokerhand1 = ""
mypokerhand2 = ""
dealer = cardobjects.DealerDeck()
hand1 = cardobjects.PlayerHand()
hand2 = cardobjects.PlayerHand()
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
        hand2.addcard(dealer.takecard())

    # Evaluate hands
    pokerhand1 = poker_objects.PokerHand(hand1.getallcards())
    pokerhand2 = poker_objects.PokerHand(hand2.getallcards())
    mypokerhand1 = pokerhand1.pokerhand[__hand]
    mypokerhand2 = pokerhand2.pokerhand[__hand]

    # Count hand types
    if mypokerhand1 != "High Card":
        pass

    if mypokerhand1 in pokerhands1:
        pokerhands1[mypokerhand1] += 1
    else:
        pokerhands1[mypokerhand1] = 1

    if mypokerhand2 in pokerhands2:
        pokerhands2[mypokerhand2] += 1
    else:
        pokerhands2[mypokerhand2] = 1

    # return cards back to deck
    for hands in range(0, 5):
        dealer.addcard(hand1.takecard())
        dealer.addcard(hand2.takecard())

# Print summary of all rounds
print(f"{'Hands':<15}{'Player 1':>10}{'Player 2':>10}")
print(f"{'-----':<15}{'--------':>10}{'--------':>10}")

for item in pokerhands1:
    print(f"{item:<15}{pokerhands1[item]:>10}{pokerhands2[item]:>10}")

print()
print("End Of Simulation")
#wait = input("Press ENTER to continue.")
