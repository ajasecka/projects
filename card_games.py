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


# card postions for (T)rump list and (N)ot (T)rump list
LIST_T = ['9', '10', 'J', 'Q', 'K', 'A', 'J2', 'J1']
LIST_NT = ['9', '10', 'J', 'Q', 'K', 'A']


# chooses a card for the CPU to play
# very simple choosing for now for testing
# input(s): list (of player's cards)
def choose_card(player):
    pass


# displays the probability of each card winning that current hand
def cards_probability(you, unknown, table, trump):
    '''
    calculating probability of card winning:
    check how many people left can play
    check if next players have the suit
    determine probability of card winning
    IF NO CARDS CAN WIN: determine worst card to play (remove lowest card or something not too in depth)
    Improvements: determine which card is best to play overall (in the hand) rather than just that specific turn
    '''

    print(table)
    first = None

    # if first card
    if table.count('_') == 4:
        print('first card')
        first = True
    else:
        print('not first card')
        first = False

    # going through your cards
    for suit in you.keys():
        for card in you[suit]:
            lose = 0
            tot = 0
            # going through unknown cards
            for u_suit in unknown.keys():
                for u_card in unknown[u_suit][0]:
                    if first:
                        if suit == trump:
                            if u_suit == trump:
                                if LIST_T.index(u_card) > LIST_T.index(card):
                                    lose += 1
                        else:
                            if u_suit == trump:
                                lose += 1
                            elif u_suit == suit:
                                if LIST_NT.index(u_card) > LIST_NT.index(card):
                                    lose += 1
                    tot += 1
            print(f'card: {suit}{card}: {tot - lose}/{tot}')




# dealing cards to each of the four players
# input(s):   N/A
# output(s):  list (of trump card + remaining cards in order)
#           list (of list of players' hands)
def deal_cards():
    # initializing hands
    h1 = {'T': [], '1': [], '2': [], '3': []}
    h2 = {'T': [], '1': [], '2': [], '3': []}
    h3 = {'T': [], '1': [], '2': [], '3': []}
    h4 = {'T': [], '1': [], '2': [], '3': []}
    hands = [h1, h2, h3, h4]
    cards = ['TA', 'TK', 'TQ', 'TJ1', 'T10', 'T9', 'TJ2',
             '1A', '1K', '1Q', '110', '19',
             '2A', '2K', '2Q', '2J', '210', '29',
             '3A', '3K', '3Q', '3J', '310', '39']

    # choosing trump card
    trump = random.randint(0, 5)
    remaining = [cards[trump]]
    cards.pop(trump)

    # randomly dealing hands
    for hand in hands:
        for _ in range(5):
            choose = random.randint(0, len(cards) - 1)
            hand[cards[choose][0]].append(cards[choose][1:])
            cards.pop(choose)

    # adding trump card to remaining hand (set as the first position in the list)
    remaining += cards

    return remaining, [h1, h2, h3, h4]


def main():
    dealer = random.randint(0, 3)
    score = [0, 0]

    while score[0] < 10 and score[1] < 10:
        # initializations
        table = ['_', '_', '_', '_']
        # player order: you, opp1, partner, opp2 (for consistency with dealing)
        remaining, players = deal_cards()
        you = players[0]
        print(f'remaining: {remaining}')
        print(f'you: {you}')
        print(f'partner: {players[2]}')
        print(f'opp1: {players[1]}')
        print(f'opp2: {players[3]}')

        trump = remaining[0]
        # list of which cards are still playable and which players definitely do not have this suit
        unknown = {'T': [['J1', 'J2', 'A', 'K', 'Q', '10', '9'], [False, False, False]],
                   '1': [['A', 'K', 'Q', '10', '9'], [False, False, False]],
                   '2': [['A', 'K', 'Q', 'J', '10', '9'], [False, False, False]],
                   '3': [['A', 'K', 'Q', 'J', '10', '9'], [False, False, False]]}

        # removing your cards and trump card from unknown cards
        for suit in you.keys():
            for your_cards in you[suit]:
                unknown[suit][0].remove(your_cards)

        # removing trump card from unknown cards
        unknown['T'][0].remove(trump[1:])
        print(f'unknown: {unknown}')

        # choose trump
        # TODO LOGIC FOR CHOOSING TRUMP
        trump = trump[0]

        # playing cards
        # TODO LOOP HERE TO GO THROUGH ALL CARDS IN HAND (range(5))
        for x in range(4):
            whos_turn = (x + dealer) % 4  # TODO WRONG, NEED TO SEE WHO WON, ONLY USE THIS FOR FIRST CARD
            if whos_turn == 0:
                cards_probability(you, unknown, table, trump)
                input('Choose card (dictionary key followed by value): ')
                # TODO CHECK IF CARD EXISTS
                # TODO ADD CARD TO PILE
            else:
                chosen_card = choose_card(players[whos_turn])
                # table[whos_turn] = chosen_card
                # unknown[chosen_card[0]].remove(chosen_card[1:])

        # TODO DECIDE BEST CARD, ADD TO "HAND SCORE", REPEAT "PLAYING CARDS" UNTIL ALL CARDS ARE GONE



if __name__ == '__main__':
    main()