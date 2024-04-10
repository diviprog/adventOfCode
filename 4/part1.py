def main():
    inf = open("input.txt", "r")
    cards = []
    for i in inf:
        cards.append(i)

    total = 0
    for i in cards:
        winning_cards = []
        have_cards = []
        number = 0
        for j in range(10, 40):
            if i[j].isdigit():
                number = 10*number + int(i[j])
            elif i[j] == ' ' and number != 0:
                winning_cards.append(number)
                number = 0

        number = 0
        for j in range(42,len(i)):
            if i[j].isdigit():
                number = 10 * number + int(i[j])
            elif number != 0:
                have_cards.append(number)
                number = 0

        score = 0
        for j in winning_cards:
            if j in have_cards:
                if score == 0:
                    score = 1
                else:
                    score *= 2

        total += score

    print(total)


main()