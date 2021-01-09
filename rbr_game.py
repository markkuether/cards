import cardobjects


def card_colors(deck):
    pass


one_deck = cardobjects.DealerDeck()
one_deck.makedeck()
one_deck.shufflecards()
player1 = cardobjects.PlayerHand()
player2 = cardobjects.PlayerHand()
compare = cardobjects.PlayerHand()

for loop in range(3):
    player1.addcard(one_deck.takecard())

for loop in range(3):
    player2.addcard(one_deck.takecard())

player1.showcards()

player2.showcards()
