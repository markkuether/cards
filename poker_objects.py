class PokerHand:
    __cardface = 0
    __cardsuite = 1
    __cardvalue = 2

    def __init__(self, hand):
        self.__hand = hand
        self.__pokerhand = []
        self.__evaluate(self.__hand)

    def __evaluate(self, hand):
        bFlush = True
        bStraight = True
        bFourKind = False
        bThreeKind = False
        bTwoKind = False
        bTwoPair = False
        bPair = False
        bHighCard = True

        self.__hand.sort(
            key=lambda card: card[self.__cardvalue], reverse=True)
        highcard = self.__hand[0]

        # Flush?
        suite = ""
        allsuites = ""
        num = 0
        for card in self.__hand:
            num += 1
            allsuites += card[self.__cardsuite]
            suite = card[self.__cardsuite]*num
            if suite != allsuites:
                bFlush = False
                break

        # Straight?
        nextval = highcard[self.__cardvalue]
        for card in self.__hand:
            cardval = card[self.__cardvalue]
            if cardval != nextval:
                bStraight = False
                break
            nextval -= 1

        # CountKind
        kindcount = {}
        for card in self.__hand:
            thisface = card[self.__cardface]
            if thisface in kindcount:
                kindcount[thisface] += 1
            else:
                kindcount[thisface] = 1

        twopair = 0
        for thisface, count in kindcount.items():
            if count == 4:
                bFourKind = True
            if count == 3:
                bThreeKind = True
            if count == 2:
                bTwoKind = True
                twopair += 1
        if twopair == 2:
            bTwoPair = True

        # Set Hand
        thishand = "High Card"
        if bTwoKind:
            thishand = "Two Kind"
        if bTwoPair:
            thishand = "Two Pair"
        if bThreeKind:
            thishand = "Three Kind"
        if bStraight:
            thishand = "Straight"
        if bFlush:
            thishand = "Flush"
        if bTwoKind and bThreeKind:
            thishand = "Full House"
        if bFourKind:
            thishand = "Four Kind"
        if bStraight and bFlush:
            thishand = "Straight Flush"

        self.__pokerhand = [thishand, highcard]

    @property
    def pokerhand(self):
        return self.__pokerhand
