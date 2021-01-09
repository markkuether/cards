# Four Hand Stats - if you deal four hands of cards
# from x decks, what are the chances of dealing y hand?
# Dealing sequential instead of standard

import cardobjects
import poker_objects
__hand = 0

# Number of times to play.
rounds = 1000
decks = 1
print()
print("*** FOUR HAND STATS ***")
print(f"Count types of hands delt to four hands from {decks} deck of cards.")
print("(Cards Delt Sequentially)")
# Set initial hand types for output at end.
pokerhands1 = {"High Card": 0, "Two Kind": 0, "Two Pair": 0, "Three Kind": 0,
               "Straight": 0, "Flush": 0, "Full House": 0, "Four Kind": 0, "Straight Flush": 0}
pokerhands2 = {"High Card": 0, "Two Kind": 0, "Two Pair": 0, "Three Kind": 0,
               "Straight": 0, "Flush": 0, "Full House": 0, "Four Kind": 0, "Straight Flush": 0}
pokerhands3 = {"High Card": 0, "Two Kind": 0, "Two Pair": 0, "Three Kind": 0,
               "Straight": 0, "Flush": 0, "Full House": 0, "Four Kind": 0, "Straight Flush": 0}
pokerhands4 = {"High Card": 0, "Two Kind": 0, "Two Pair": 0, "Three Kind": 0,
               "Straight": 0, "Flush": 0, "Full House": 0, "Four Kind": 0, "Straight Flush": 0}

# Initialize variables & Create Objects
mypokerhand1 = ""
mypokerhand2 = ""
mypokerhand3 = ""
mypokerhand4 = ""

dealer = cardobjects.DealerDeck()
hand1 = cardobjects.PlayerHand()
hand2 = cardobjects.PlayerHand()
hand3 = cardobjects.PlayerHand()
hand4 = cardobjects.PlayerHand()

dealer.makedeck(decks)

# Print header and start
print(f"Dealing {rounds} rounds:")
print("========================")
print()
for trials in range(0, rounds):
    dealer.shufflecards()

   # Deal Cards - Sequentially
    for cards in range(0, 5):
        hand1.addcard(dealer.takecard())

    for cards in range(0, 5):
        hand2.addcard(dealer.takecard())

    for cards in range(0, 5):
        hand3.addcard(dealer.takecard())

    for cards in range(0, 5):
        hand4.addcard(dealer.takecard())

    # Evaluate Hands
    pokerhand1 = poker_objects.PokerHand(hand1.getallcards())
    pokerhand2 = poker_objects.PokerHand(hand2.getallcards())
    pokerhand3 = poker_objects.PokerHand(hand3.getallcards())
    pokerhand4 = poker_objects.PokerHand(hand4.getallcards())

    mypokerhand1 = pokerhand1.pokerhand[__hand]
    mypokerhand2 = pokerhand2.pokerhand[__hand]
    mypokerhand3 = pokerhand3.pokerhand[__hand]
    mypokerhand4 = pokerhand4.pokerhand[__hand]

    # Count Hand Types
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

    if mypokerhand3 in pokerhands3:
        pokerhands3[mypokerhand3] += 1
    else:
        pokerhands3[mypokerhand3] = 1

    if mypokerhand4 in pokerhands4:
        pokerhands4[mypokerhand4] += 1
    else:
        pokerhands4[mypokerhand4] = 1

    # return cards back to deck
    for hands in range(0, 5):
        dealer.addcard(hand1.takecard())
        dealer.addcard(hand2.takecard())
        dealer.addcard(hand3.takecard())
        dealer.addcard(hand4.takecard())

# Print summary of all rounds
print(f"{'Hands':<15}{'Player 1':>10}{'Player 2':>10}{'Player 3':>10}{'Player 4':>10}")
print(f"{'-----':<15}{'--------':>10}{'--------':>10}{'--------':>10}{'--------':>10}")

for item in pokerhands1:
    print(
        f"{item:<15}{pokerhands1[item]:>10}{pokerhands2[item]:>10}{pokerhands3[item]:>10}{pokerhands4[item]:>10}")
print()
print("End Of Simulation")
#wait = input("Press ENTER to continue.")
