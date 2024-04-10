def main():
    inf = open("input.txt", "r")

    max_red = 12
    max_green = 13
    max_blue = 14

    total = 0
    for i in inf:
        possible = True
        for j in range(len(i)):
            if i[j].isdigit() and i[j + 1].isdigit():
                if (i[j + 3:j + 6] == "red") and (int(i[j]) * 10 + int(i[j + 1]) > max_red):
                    possible = False
                elif (i[j + 3:j + 8] == "green") and (int(i[j]) * 10 + int(i[j + 1]) > max_green):
                    possible = False
                elif (i[j + 3:j + 7] == "blue") and (int(i[j]) * 10 + int(i[j + 1]) > max_blue):
                    possible = False

        if possible:
            if i[6].isdigit():
                total += int(i[5])*10 + int(i[6])
            else:
                total += int(i[5])

    print(total)


main()
