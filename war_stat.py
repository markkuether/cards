import cardobjects
import war_objects
import math

""" War Rules

Decks:
- The full number of decks is evenly divided
between players.
- 'Wins' are placed at the bottom of the deck.
- If the number of cards is uneven, the remaining
cards are discarded for the game so no player has
an advantage.

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
bottom of a players deck.
"""
# Default Values
playercount = 2
deckcount = 1
conflictsize = 3
gamecount = 10
battle_limit = 25000

# Calculations
average_battles = 0
median_battles = 0

all_counts = []
for games in range(gamecount):
    my_players = war_objects.Players(playercount, deckcount)
    battles = 0
    while my_players.active_players > 1 and battles < battle_limit:
        battles += 1
        result = my_players.battle()
        if result == "WAR":
            my_players.draw(3)
        else:
            winner_num = int(result)
            my_players.cards_to_winner(winner_num)

    print(f"WINNER: {winner_num+1} in {battles} rounds")
    del my_players
    all_counts.append(battles)

all_counts.sort()
average_battles = sum(all_counts)/len(all_counts)
if len(all_counts) % 2 == 0:
    median_battles = (all_counts[gamecount//2] +
                      all_counts[(gamecount//2)+1])/2
else:
    median_battles = (all_counts[(gamecount//2)+1])

print()
print(f"AVERAGE GAME LENGTH: {int(average_battles//1)} rounds")
print(f"MEDIAN GAME LENGTH: {int(median_battles//1)} rounds")
print(f"MIN GAME LENGTH: {min(all_counts)} rounds")
print(f"MAX GAME LENGTH: {max(all_counts)} rounds")
