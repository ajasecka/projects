# use computer vision to see the cards (can be added later)

# euchre probability calculator (per round, your hand probability alone / your hand + partner hand)
# the "1" dictionary is the left bower suit, which will not have a jack in it, slightly distorting the probability

# black jack / 21 probability

"""
probability of not drawing face card:
40 * 39 * 38 * 37
-----------------
52 * 51 * 50 * 49

or

(40) /  (52)
( 4) /  ( 4)

https://math.stackexchange.com/questions/3404961/drawing-at-least-one-face-card-without-replacement-in-four-attempts-take-the-be
"""

import random


# displays the probability of each card winning that current hand
def cards_probability():
    pass


# returns which suit the card is a part of
def choose_dict(card):
    return 'trump' if card[0] == 'T' else '1' if card[0] == 'O' else '2' if card[0] == 'X' else '3'


# dealing cards to each of the four players
def deal_cards():
    # initializing hands
    h1 = {'trump': [], '1': [], '2': [], '3': []}
    h2 = {'trump': [], '1': [], '2': [], '3': []}
    h3 = {'trump': [], '1': [], '2': [], '3': []}
    h4 = {'trump': [], '1': [], '2': [], '3': []}
    hands = [h1, h2, h3, h4]
    cards = ['TA', 'TK', 'TQ', 'TJ1', 'T10', 'T9', 'TJ2',
             'OA', 'OK', 'OQ', 'O10', 'O9',
             'XA', 'XK', 'XQ', 'XJ', 'X10', 'X9',
             'YA', 'YK', 'YQ', 'YJ', 'Y10', 'Y9']

    # choosing trump card
    trump = random.randint(0, 5)
    remaining = [cards[trump]]
    cards.pop(trump)

    # randomly dealing hands
    for hand in hands:
        for _ in range(5):
            choose = random.randint(0, len(cards) - 1)
            hand[choose_dict(cards[choose])].append(cards[choose][1:])
            cards.pop(choose)

    # adding trump card to remaining hand (set as the first position in the list)
    remaining += cards

    return remaining, h1, h2, h3, h4


def main():
    remaining, you, partner, opp1, opp2 = deal_cards()
    print(f'remaining: {remaining}')
    print(f'you: {you}')
    print(f'partner: {partner}')
    print(f'opp1: {opp1}')
    print(f'opp2: {opp2}')

    trump = remaining[0]
    unknown = {'trump':     ['J1', 'J2', 'A', 'K', 'Q', '10', '9'],
               '1':         ['A', 'K', 'Q', '10', '9'],
               '2':         ['A', 'K', 'Q', 'J', '10', '9'],
               '3':         ['A', 'K', 'Q', 'J', '10', '9']}

    # removing your cards and trump card from unknown cards
    for suit in you.keys():
        for your_cards in you[suit]:
            unknown[suit].remove(your_cards)

    unknown['trump'].remove(trump[1:])
    print(f'unknown: {unknown}')

    cards_probability(you)



if __name__ == '__main__':
    main()