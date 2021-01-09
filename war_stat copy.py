import cardobjects
import sys
import time

""" War Rules

Decks:
- The full number of decks is evenly divided
between players.
- 'Wins' are placed at the bottom of the deck.
- If the number of cards is uneven, the remaining
cards are discarded for the game so no player has
an advantage.

Rules:
- Ace acts as high card
- Suite is neutral - no heirarchy
- In conflict - high card wins all cards.
- In tied conflicts:
- - All parties draws n cards face down.
- - All parties draws n+1 card face up.
- - High card for n+1 card wins all cards.
- - Tie repeats with n + 1 more cards drawn.
- - Any party unable to produce all cards loses.

Shuffling:
- Each 'win' is shuffled before adding to the
bottom of a players deck.
"""
# Default Values
playercount = 2
deckcount = 1
conflictsize = 3
gamecount = 1

# Default Limits
playermin = 2
playermax = 10
deckmin = 1
deckmax = 10
conflictmin = 1
conflictmax = 3
gamemin = 1
gamemax = 1000


def checkparams():
    # Gather Game Details:
    # Player count, Deck Count, Conflict Size, Game Count

    optlen = len(sys.argv)

    if optlen > 1 and optlen < 5:
        print("You need to enter 4 parameters to play.")
        optlen = 1

    if optlen == 5:
        # Check to make sure all are numeric
        bNumber = False
        truecount = 0
        for item in range(1, 5):
            param = str(sys.argv[item])
            if param.isdigit() or len(param) < 6:
                truecount += 1

        if truecount == 4:
            bNumber = True
        else:
            optlen = 1
            print("Those values are not acceptable for WAR.")

        rangecount = 0
        if bNumber:
            getplayercount = int(sys.argv[1])
            getdeckcount = int(sys.argv[2])
            getconflictsize = int(sys.argv[3])
            getgamecount = int(sys.argv[4])

            if playermin <= getplayercount <= playermax:
                rangecount += 1
            if deckmin <= getdeckcount <= deckmax:
                rangecount += 1
            if conflictmin <= getconflictsize <= conflictmax:
                rangecount += 1
            if gamemin <= getgamecount <= gamemax:
                rangecount += 1

            if rangecount == 4:
                playercount = getplayercount
                deckcount = getdeckcount
                conflictsize = getconflictsize
                gamecount = getgamecount
            else:
                print("Input values are out of range.")
                optlen = 1

    if optlen == 1:
        getparams()


def getparams():
    enterplayercount = input("How many players will there be? (2-10 def=2) ")
    enterdeckcount = input(
        "How many decks of cards should there be? (1-10 def=1) ")
    enterconflictsize = input(
        "With a tie (war), how many cards get laid down (1-3 def=3) ")
    entergamecount = input(
        "How many games did you wish to simulate (1-1000 def=1) ")

    playercount = enterplayercount
    deckcount = enterdeckcount
    conflictsize = enterconflictsize
    gamecount = entergamecount


# Create and shuffle Decks
def create_decks(deck_count: int):
    all_decks = cardobjects.DealerDeck()
    all_decks.makedeck(decks=deck_count)
    all_decks.shufflecards()
    return all_decks


def deal_cards(deck, players):

    while deck.cardcount > 0:
        for player in players:
            player.addcard(deck.takecard())
    return True

# Conflict - players = list of player decks.  Piles = list of pile decks
# This assumes at least 1 card in pile.


def play_conflict(players, piles):
    max = -1
    winner = -1
    value = 2
    war = False
    for p_number, player in enumerate(players):
        if player.cardcount > 0:
            card = player.takecard()
            piles[p_number].addcard(card)
            if card[value] == max:
                war = True
            elif card[value] > max:
                max = card[value]
                winner = p_number
    if war:
        return -1
    else:
        return winner


# War
def war(players, piles, drawnum: int):
    losers = []
    for p_number, player in enumerate(players):
        if player.cardcount > 0:
            draw_count = 0
            while draw_count < drawnum:
                piles[p_number].addcard(player.takecard())
                draw_count += 1
                if player.cardcount == 0:
                    losers.append(p_number)
                    break
    return losers


def givecards(players, piles, winner):
    for p_number, player in enumerate(players):
        if p_number != winner:
            while piles[p_number].cardcount > 0:
                piles[winner].addcard(piles[p_number].takecard())
    piles[winner].shufflecards
    while piles[winner].cardcount > 0:
        players[winner].addcard(piles[winner].takecard())

    return True


def print_stats(players):
    time.sleep(1)
    for num_player, player in enumerate(players):
        print(f"Player {num_player+1}: {player.cardcount} cards", end=" | ")
    print()


num_of_players = 2
num_of_draws = 3
playerlist = []
activelist = []
pilelist = []
loser_num_set = set([])
fullplayer = []
no_winner = -1

# list of winners.
# list of losers.

whole_deck = create_decks(1)
for one_player in range(num_of_players):
    this_player = cardobjects.PlayerHand()
    playerlist.append(this_player)
    activelist.append(this_player)
    pilelist.append(cardobjects.PlayerHand())

done = deal_cards(whole_deck, playerlist)
the_winner = no_winner
conflict_count = 0
while len(loser_num_set) < (num_of_players-1):
    the_winner = play_conflict(playerlist, pilelist)
    conflict_count += 1

    for num, player in enumerate(playerlist):
        if (player.cardcount == 0) and (num not in loser_num_set):
            loser_num_set.add(num)
    if the_winner > no_winner:
        givecards(playerlist, pilelist, the_winner)
    else:
        # war
        loser_num_set.append(war(playerlist, pilelist, num_of_draws))
    print_stats(playerlist)

for num, player in enumerate(playerlist):
    if num not in loser_num_set:
        print(f"Player {num+1} WINS in {conflict_count} battles.")
        break


# Present Stats
# print(len(sys.argv))
# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])
# print(sys.argv[3])
# print(sys.argv[4])

# checkparams()
#print(f"players = {playercount}")
#print(f"decks = {deckcount}")
#print(f"conflicts = {conflictsize}")
#print(f"games = {gamecount}")

'''
main = cardobjects.DealerDeck()
player1 = cardobjects.PlayerHand()
player2 = cardobjects.PlayerHand()
discard = cardobjects.PlayerHand()
pile1 = cardobjects.PlayerHand()
pile2 = cardobjects.PlayerHand()

main.makedeck()
allcards = main.cardcount

main.shufflecards()
even = True
# deal cards to 2 players
for card in range(main.cardcount):
    if even:
        player1.addcard(main.takecard())
    else:
        player2.addcard(main.takecard())
    even = not even

pile1.addcard(player1.takecard())
pile2.addcard(player2.takecard())

# battle
if pile1.getcardval > pile2.getcardval:
    pile1.addcard(pile2.takecard())
    pile1.shufflecards
    for card in range(pile1.cardcount):
        player1.addcard(pile1.takecard())

elif pile1.getcardval < pile2.getcardval:
    pile2.addcard(pile1.takecard())
    pile2.shufflecards
    for card in range(pile2.cardcount):
        player2.addcard(pile2.takecard())

else:
    # WAR!
    stop = False
    while not stop:
        pass
'''
