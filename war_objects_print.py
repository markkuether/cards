import cardobjects
import random
import time


class Player:
    def __init__(self, id: int):
        self.__player_deck = cardobjects.PlayerHand()
        self.__card_count = 0
        self.__player_id = id
        self.__is_active = True

    def take_card(self, card: tuple):
        """
        Receives one card object and adds it to
        the players deck.
        Sets player active status to True.
        """

        self.__player_deck.addcard(card)
        self.__is_active = True

    def give_card(self):
        """
        Generates player_card (3-tuple) containing
        the card object, the player ID, the player status.
        Sets the active status to False if all cards used.

        Returns the player_card to caller.
        """
        next_card = ()
        state_list = []
        player_card = (next_card, self.__player_id, self.__is_active)

        if self.__player_deck.cardcount > 0:
            next_card = self.__player_deck.takecard()
            player_card = (next_card, self.__player_id, self.__is_active)

        if self.__player_deck.cardcount == 0:
            self.__is_active = False
        return player_card

    def report(self, all_cards: bool = False):
        """
        Prints the number of cards in the users deck
        if they are active. Contains logic for 
        showing all user cards, which is disabled 
        by default.
        """
        if self.is_active:
            print(
                f"{self.__player_id+1}){self.__player_deck.cardcount}", end=" ")

            if 0 == 1:
                # if all_cards:
                print()
                my_cards = self.__player_deck.getallcards()
                for card in my_cards:
                    print(f"{card[0]}{card[1]} ", end="")
                print()

    @property
    def card_count(self):
        return self.__player_deck.cardcount

    @property
    def player_id(self):
        return self.__player_id

    @property
    def is_active(self):
        return self.__is_active


class Players:
    def __init__(self, number_of_players: int = 2, number_of_decks: int = 1):
        self.__player_list = []
        self.__main_deck = cardobjects.DealerDeck()
        self.__main_deck.makedeck(number_of_decks)
        self.__main_deck.shufflecards()
        self.__battlefield = Battlefield(number_of_players)
        self.__winner = 0
        self.__active_players = number_of_players

        if not (1 < number_of_players < 11):
            print("You can only have between 2 and 10 players. \n")
            raise ValueError()
        if not (0 < number_of_decks < 6):
            print("You can only have between 1 and 5 decks. \n")
            raise ValueError()

        for player_num in range(number_of_players):
            self.__player_list.append(Player(player_num))

        self.__deal_cards(self.__main_deck, self.__player_list)

    def __deal_cards(self, card_deck, player_list):
        if card_deck.cardcount % len(player_list) != 0:
            print(f"{card_deck.cardcount} cards cannot be evenly", end=" ")
            print(f"distributed between {self.__active_players} players.\n")
            raise ValueError()

        while card_deck.cardcount > 0:
            for player in player_list:
                player.take_card(card_deck.takecard())

    def battle(self):
        """
        places cards in battlefield for all
        active players. returns result as
        string
        """
        result = ""
        for player in self.__player_list:
            if player.is_active:
                print(f"{player.player_id+1})", end="")
            self.__battlefield.take_card(player.give_card())
        print(" --> ", end="")
        result = self.__battlefield.evaluate()
        return result

    def draw(self, draw_count):
        """
        passes cards to battlefield
        in prep for war.
        """
        print("WAR! ", end="")
        for player in self.__player_list:
            if player.is_active:
                num = 0
                print(f"{player.player_id+1})", end="")
                while num < draw_count:
                    self.__battlefield.take_card(player.give_card())
                    num += 1
                print(" | ", end="")
        print()

    def cards_to_winner(self, winner_num: int):
        """
        Retrieves all cards from the battlefield.
        Gives all cards to the winner.
        """
        all_cards = self.__battlefield.return_cards()
        for card in all_cards:
            self.__player_list[winner_num].take_card(card)

    def report(self):
        """
        Calls player report. Includes logic for printing
        all cards from player for tracing purposes.
        This is hard coded to a 1 deck size.
        Optionally adds delay so game plays in human time.
        """
        for player in self.__player_list:
            if player.card_count > 46 or player.card_count < (52-46):
                player.report(True)
            else:
                player.report(False)
        print("")
        time.sleep(0)

    @property
    def active_players(self):
        active_count = 0
        for player in self.__player_list:
            if player.is_active:
                active_count += 1
        return active_count

    @property
    def winner(self):
        return self.__winner

    @winner.setter
    def winner(self, winner: int):
        self.__winner = winner


class Battlefield:
    def __init__(self, number_of_players):
        self.__battle_list = []
        self.__active_list = []
        self.__battle_size = -1
        for player_num in range(number_of_players):
            self.__battle_list.append(cardobjects.PlayerHand())
            self.__active_list.append(False)

    def take_card(self, player_card):
        """
        Receives player_cards and unpacks them.
        Adds card objects to battle, contained in battlefield list.
        Tracks size of the battle.
        """
        card, player, is_active = player_card
        if is_active:
            if card[0] != "10":
                print(f" {card[0]}{card[1]}", end=" ")
            else:
                print(f"{card[0]}{card[1]}", end=" ")
        self.__active_list[player] = is_active
        if is_active == True:
            self.__battle_list[player].addcard(card)
            if self.__battle_list[player].cardcount > self.__battle_size:
                self.__battle_size += 1

    def evaluate(self):
        """
        Determines the high card of all players.
        Status string is set to the id of the winner.
        In case of tie, sets status to "WAR".

        Returns status string to caller.
        """
        state = ""
        card_val = 2
        high_card = -1
        battle_val = -1

        for num, battle in enumerate(self.__battle_list):
            if self.__active_list[num]:
                if battle.get_value(battle.cardcount) > high_card:
                    state = str(num)
                    high_card = battle.get_value(battle.cardcount)
                elif battle.get_value(battle.cardcount) == high_card:
                    state = "WAR"
        return state

    def return_cards(self):
        """
        Combines all cards in battle_list to a single
        list.  Shuffles all cards.  
        Returns list of cards to caller.
        """
        all_cards = []
        for battle in self.__battle_list:
            while battle.cardcount > 0:
                all_cards.append(battle.takecard())
        random.shuffle(all_cards)
        self.__battle_size = -1
        return all_cards


# player object
# - ID
# - hand
# - pile
# - cardcount
# - state

# all_players object
# all players
# method conflict
# method war
