from collections import Counter

def checkfiveofkind(hand):
    dct = Counter(hand)
    if (5-dct['J'] or 5) in dct.values():
        return True

def checkfourofkind(hand):
    dct = Counter(hand)
    if (4-dct['J'] or 4) in dct.values():
        return True

def checktwopair(hand):
    dct = Counter(hand)
    if Counter(dct.values())[2] > 1 or (checkpair(hand) and (dct['J'] == 1 or dct['J'] == 2)):
        return True

def checkfullhouse(hand):
    if checktrips(hand) and checkpair(hand):
        return True

def checktrips(hand):
    dct = Counter(hand)
    if (3 or 3-dct['J']) in dct.values():
        return True

def checkpair(hand):
    dct = Counter(hand)
    if (2 or 2-dct['J']) in dct.values():
        return True


def besthand(hand):
    if checkfiveofkind(hand):
        return 7
    elif checkfourofkind(hand):
        return 6
    elif checkfullhouse(hand):
        return 5
    elif checktrips(hand):
        return 4
    elif checktwopair(hand):
        return 3
    elif checkpair(hand):
        return 2
    else:
        return 1


def comparehands(hand1, hand2):
    if besthand(hand1) > besthand(hand2):
        return -1
    elif besthand(hand1) < besthand(hand2):
        return 1
    else:
        translation = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 1, 'Q': 12, 'K': 13,
                   'A': 14}
        for i in range(len(hand1)):
            if translation[hand1[i]] > translation[hand2[i]]:
                return -1
            elif translation[hand1[i]] < translation[hand2[i]]:
                return 1
    return 0


def main():
    inf = open("input.txt", "r")
    lines = []
    for i in inf:
        lines.append(i)

    hands = []
    bids = []
    for i in lines:
        string = ""
        number = 0
        space = False
        for j in i:
            if j == ' ':
                space = True

            if space and j!=' ' and j!='\n':
                number = 10*number + int(j)
            elif not space:
                string += j
        hands.append(string)
        bids.append(number)

    ordered_hands = [hands[0]]
    ordered_bids = [bids[0]]
    for i in range(1, len(hands)):
        j = 0
        while j < len(ordered_hands) and comparehands(hands[i], ordered_hands[j]) == -1:
            j += 1
        ordered_hands.insert(j, hands[i])
        ordered_bids.insert(j, bids[i])
        print(hands[i], Counter(hands[i]), besthand(hands[i]))
        if i == 5:
            break

    sum = 0
    for i in range(len(ordered_bids)):
        sum += (i+1)*ordered_bids[i]

    print(sum)


main()