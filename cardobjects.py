import random
import math


class Deck:
    __cardface = 0
    __cardsuite = 1
    __cardvalue = 2

    def __init__(self):
        self.__cards = []
        self.__shuffled = False

    def shufflecards(self):
        random.shuffle(self.__cards)
        self.__shuffled = True

    def takecard(self, cardpos=0):
        if (len(self.__cards) > 0) and (cardpos > -1):
            if cardpos > len(self.__cards):
                cardpos = len(self.__cards)
            return self.__cards.pop(cardpos)
        else:
            return ("empty", "empty", 0)

    def addcard(self, cardtuple):
        self.__cards.append(cardtuple)

    def showcards(self):
        for card in self.__cards:
            face = card[self.__cardface]
            suite = card[self.__cardsuite]
            print(f"{face}{suite}", end=" ")

    def get_face(self, pos: int):
        if pos <= len(self.__cards):
            return self.__cards[pos-1][0]
        else:
            return ""

    def get_suite(self, pos: int):
        if pos <= len(self.__cards):
            return self.__cards[pos-1][1]
        else:
            return ""

    def get_value(self, pos: int):
        if pos <= len(self.__cards):
            return self.__cards[pos-1][2]
        else:
            return -1

    @property
    def cardcount(self):
        return len(self.__cards)

    @property
    def shuffled(self):
        return self.__shuffled


class DealerDeck(Deck):
    def __init__(self):
        super().__init__()
        self.__decks = 1

    def makedeck(self, decks=1, aceshigh=True):
        self.__decks = decks
        self.__aceshigh = aceshigh
        faces = ["A", "2", "3", "4", "5", "6",
                 "7", "8", "9", "10", "J", "Q", "K"]

        if self.__aceshigh == True:
            faces.append(faces.pop(0))

        suites = ["H", "D", "C", "S"]
        for deck in range(1, decks+1):
            for suite in suites:
                value = 0
                for face in faces:
                    value += 1
                    card = (face, suite, value)
                    self.addcard(card)

    def cutdeck(self, percent):
        if (self.cardcount > 1) and (percent > 0):
            dec_percent = percent/100
            cut_place = math.floor(dec_percent * self.cardcount)
            for move in range(0, cut_place+1):
                self.addcard(self.takecard())
        return "Cut"

    @property
    def deckcount(self):
        return self.__decks

    @property
    def aceshigh(self):
        return self.__aceshigh


class PlayerHand(Deck):
    def __init__(self):
        super().__init__()

    def getallcards(self):
        self.__allcards = []
        for onecard in range(0, self.cardcount):
            self.__allcards.append(self.takecard())
            self.addcard(self.__allcards[onecard])
        return self.__allcards
