def main():
    inf = open("input.txt", "r")
    cards = []
    for i in inf:
        cards.append(i)

    instances = []
    for i in range(201):
        instances.append(1)

    for i in range(len(cards)):
        winning_cards = []
        have_cards = []
        number = 0
        for j in range(10, 40):
            if cards[i][j].isdigit():
                number = 10 * number + int(cards[i][j])
            elif cards[i][j] == ' ' and number != 0:
                winning_cards.append(number)
                number = 0

        number = 0
        for j in range(42, len(cards[i])):
            if cards[i][j].isdigit():
                number = 10 * number + int(cards[i][j])
            elif number != 0:
                have_cards.append(number)
                number = 0

        matches = 0
        for j in winning_cards:
            if j in have_cards:
                matches += 1

        for j in range(i+1, i+matches+1):
            instances[j] += instances[i]

    print(sum(instances))


main()