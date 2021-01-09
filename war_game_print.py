import cardobjects
import war_objects_print

""" War Rules

Decks:
- The full number of decks must be evenly divided
between players.
- 'Wins' are placed at the bottom of the deck.

Legal Configurations

Decks   Players
=====   =======
1       2,4
2       2,4,8
3       2,3,4,6,8
4       2,4,8
5       2,4,5,8,10

Rules:
- Ace acts as high card
- Suite is neutral - no heirarchy
- In conflict - high card wins all cards.
- If high card is tied (war):
- - All parties draws n cards face down.
- - All parties draws n+1 card face up.
- - High card for n+1 card wins all cards.
- - Tie repeats with n + 1 more cards drawn.
- - Any party unable to produce all cards loses.

Shuffling:
- Each 'win' is shuffled before adding to the
bottom of the winners deck.
"""

players = 2
decks = 1
drawnum = 3
max_rounds = 25000

my_players = war_objects_print.Players(players, decks)
battles = 0
while my_players.active_players > 1 and battles < max_rounds:
    battles += 1
    print(f"Battle #{battles}: ", end="")
    result = my_players.battle()
    if result == "WAR":
        my_players.draw(drawnum)
    else:
        winner_num = int(result)
        my_players.cards_to_winner(winner_num)
        my_players.report()

print(f"WINNER: {winner_num+1} in {battles} rounds")
