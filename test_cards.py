import cardobjects


def get_cards(deckobj):
    deckobj.shufflecards()
    return True


mydeck = cardobjects.DealerDeck()
mydeck.makedeck()

card1 = mydeck.takecard()
card2 = mydeck.takecard()
btrue = get_cards(mydeck)
card3 = mydeck.takecard()
card4 = mydeck.takecard()

print(f"card1: {card1}  card2: {card2}   card3: {card3}   card4: {card4}")
