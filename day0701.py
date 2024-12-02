# create an empty list of lines
bets = []

with open("day07.txt", "r") as f:
    for line in f:
        bets.append((line.strip().split()[0], int(line.strip().split()[1])))

# print(bets)

cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
cards.reverse()


def rank(hand):

    # five of a kind
    if hand.count(hand[0]) == 5:
        return 7

    # fourofakind
    for card in hand:
        if hand.count(card) == 4:
            return 6

    # full house
    for card in hand:
        if hand.count(card) == 3:
            for card2 in hand:
                if hand.count(card2) == 2:
                    return 5

    # threeofakind
    for card in hand:
        if hand.count(card) == 3:
            return 4

    # two pair
    for card in hand:
        if hand.count(card) == 2:
            for card2 in hand:
                if card2 != card and hand.count(card2) == 2:
                    return 3

    # one pair
    for card in hand:
        if hand.count(card) == 2:
            return 2

    return 1


def rankbycard(hand):
    value = 0
    for i, card in enumerate(hand):
        # print(card, cards.index(card))
        value += 100**(4-i) * cards.index(card)
    return value


sortedbets = sorted(bets, key=lambda bet: rank(
    bet[0]) * 100000000000 + rankbycard(bet[0]))
# print(sortedbets)

total = 0
for i, bet in enumerate(sortedbets):
    total += (i+1) * bet[1]
print(total)
