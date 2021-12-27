#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()



class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        print("creating card pack")
        self.cards_pack = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("shuffling cards")
        shuffle(self.cards_pack)

    def split_into_two(self):
        return (self.cards_pack[:26], self.cards_pack[26:])


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards ".format(len(self.cards))

    def add_to_hand(self,added_cards):
        self.cards.extend(added_cards)

    def remove_cards(self):
        return self.cards.pop()

        # print(self.cards.pop())



class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_cards()

        print("{} has played {}".format(self.name,drawn_card))

        return drawn_card
        # print(drawn_card)

    def remove_war_cards(self):
        '''
        happens when two player draw same card

        '''
        war_cards = []

        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        return len(self.hand.cards) != 0


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!

d= Deck()
d.shuffle()
half1,half2=d.split_into_two()

# print(half1)
# print('\n')
# print(half2)

#creating players
comp = Player("computer",Hand(half1))

name = raw_input("What is your name? ")
user = Player(name,Hand(half2))

# print(user.hand.cards)

# c_card = comp.play_card()
# p_card = user.play_card()


total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Time for a new round")
    print("Current standing")
    print(user.name+" has count: "+str(len(user.hand.cards)))
    print(comp.name+" has count: "+str(len(comp.hand.cards)))
    print("play a card")
    print("\n")

    table_cards = []
    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if p_card[1] == c_card[1]:
        war_count +=1

        print("War!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        # c_card = comp.play_card()
        # p_card = user.play_card()
        #
        # table_cards.append(c_card)
        # table_cards.append(p_card)

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.cards.extend(table_cards)
        else:
            comp.hand.cards.extend(table_cards)

    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.cards.extend(table_cards)
        else:
            comp.hand.cards.extend(table_cards)

print("Game over after {} rounds with {} wars".format(total_rounds,war_count))
if  len(comp.hand.cards) > len(user.hand.cards):
    print("Comp is the winner")
elif len(comp.hand.cards) < len(user.hand.cards):
    print("{} is the winner!".format(name))

else:
    Print("It's a draw!")

print(comp.hand)
print(user.hand)
