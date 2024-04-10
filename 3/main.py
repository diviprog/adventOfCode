def nextSpace(line, position):
    while position < len(line) and line[position].isdigit():
        position += 1

    return position


def findNumber(line, position):
    i = 0
    number = 0
    while line[position + i].isdigit():
        number = 10 * number + int(line[position + i])
        i += 1
        if position + i >= len(line):
            break

    if line[position].isdigit():
        i = -1
        while line[position + i].isdigit():
            mult_factor = 10 ** len(str(number))
            number = mult_factor * int(line[position + i]) + number
            i -= 1
            if position + i < 0:
                break

    return number


def main():
    inf = open("input.txt", "r")
    lines = []
    for i in inf:
        lines.append(i[:140])

    total = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j].isdigit():
                if i == 0:
                    if j == 0:
                        if (lines[i][j + 1] != '.' and not (lines[i][j + 1].isdigit())) or (
                                lines[i + 1][j] != '.' and not (lines[i + 1][j].isdigit())) or (
                                lines[i + 1][j + 1] != '.' and not (lines[i + 1][j + 1].isdigit())):
                            number = findNumber(lines[i], j)
                            total += number
                            j = nextSpace(lines[i], j)
                            print(number, total, j)
                    elif j == len(lines[i]) - 1:
                        if (lines[i][j - 1] != '.' and not (lines[i][j - 1].isdigit())) or (
                                lines[i + 1][j - 1] != '.' and not (lines[i + 1][j - 1].isdigit())) or (
                                lines[i + 1][j] != '.' and not (lines[i + 1][j].isdigit())):
                            number = findNumber(lines[i], j)
                            total += number
                            j = nextSpace(lines[i], j)
                            print(number, total, j)
                    else:
                        if (lines[i][j - 1] != '.' and not (lines[i][j - 1].isdigit())) or (
                                lines[i + 1][j - 1] != '.' and not (lines[i + 1][j - 1].isdigit())) or (
                                lines[i + 1][j] != '.' and not (lines[i + 1][j].isdigit())) or (
                                lines[i + 1][j + 1] != '.' and not (lines[i + 1][j + 1].isdigit())) or (
                                lines[i][j + 1] != '.' and not (lines[i][j + 1].isdigit())):
                            number = findNumber(lines[i], j)
                            total += number
                            j = nextSpace(lines[i], j)
                            print(number, total, j)
                elif i == len(lines) - 1:
                    if j == 0:
                        if (lines[i][j + 1] != '.' and not (lines[i][j + 1].isdigit())) or (
                                lines[i - 1][j] != '.' and not (lines[i - 1][j].isdigit())) or (
                                lines[i - 1][j + 1] != '.' and not (lines[i - 1][j + 1].isdigit())):
                            number = findNumber(lines[i], j)
                            total += number
                            j = nextSpace(lines[i], j)
                            print(number, total, j)
                    elif j == len(lines[i]) - 1:
                        if (lines[i][j - 1] != '.' and not (lines[i][j - 1].isdigit())) or (
                                lines[i - 1][j - 1] != '.' and not (lines[i - 1][j - 1].isdigit())) or (
                                lines[i - 1][j] != '.' and not (lines[i - 1][j].isdigit())):
                            number = findNumber(lines[i], j)
                            total += number
                            j = nextSpace(lines[i], j)
                            print(number, total, j)
                    else:
                        if (lines[i][j - 1] != '.' and not (lines[i][j - 1].isdigit())) or (
                                lines[i - 1][j - 1] != '.' and not (lines[i - 1][j - 1].isdigit())) or (
                                lines[i - 1][j] != '.' and not (lines[i - 1][j].isdigit())) or (
                                lines[i - 1][j + 1] != '.' and not (lines[i - 1][j + 1].isdigit())) or (
                                lines[i][j + 1] != '.' and not (lines[i][j + 1].isdigit())):
                            number = findNumber(lines[i], j)
                            total += number
                            j = nextSpace(lines[i], j)
                            print(number, total, j)
                else:
                    if j == 0:
                        if (lines[i][j + 1] != '.' and not (lines[i][j + 1].isdigit())) or (
                                lines[i - 1][j] != '.' and not (lines[i - 1][j].isdigit())) or (
                                lines[i + 1][j] != '.' and not (lines[i + 1][j].isdigit())) or (
                                lines[i + 1][j + 1] != '.' and not (lines[i + 1][j + 1].isdigit())) or (
                                lines[i - 1][j + 1] != '.' and not (lines[i - 1][j + 1].isdigit())):
                            number = findNumber(lines[i], j)
                            total += number
                            j = nextSpace(lines[i], j)
                            print(number, total, j)
                    elif j == len(lines[i]) - 1:
                        if (lines[i][j - 1] != '.' and not (lines[i][j - 1].isdigit())) or (
                                lines[i - 1][j] != '.' and not (lines[i - 1][j].isdigit())) or (
                                lines[i + 1][j] != '.' and not (lines[i + 1][j].isdigit())) or (
                                lines[i + 1][j - 1] != '.' and not (lines[i + 1][j - 1].isdigit())) or (
                                lines[i - 1][j - 1] != '.' and not (lines[i - 1][j - 1].isdigit())):
                            number = findNumber(lines[i], j)
                            total += number
                            j = nextSpace(lines[i], j)
                            print(number, total, j)
                    else:
                        if (lines[i][j - 1] != '.' and not (lines[i][j - 1].isdigit())) or (
                                lines[i][j + 1] != '.' and not (lines[i][j + 1].isdigit())) or (
                                lines[i - 1][j] != '.' and not (lines[i - 1][j].isdigit())) or (
                                lines[i + 1][j] != '.' and not (lines[i + 1][j].isdigit())) or (
                                lines[i + 1][j - 1] != '.' and not (lines[i + 1][j - 1].isdigit())) or (
                                lines[i - 1][j - 1] != '.' and not (lines[i - 1][j - 1].isdigit())) or (
                                lines[i + 1][j + 1] != '.' and not (lines[i + 1][j + 1].isdigit())) or (
                                lines[i - 1][j + 1] != '.' and not (lines[i - 1][j + 1].isdigit())):
                            number = findNumber(lines[i], j)
                            total += number
                            j = nextSpace(lines[i], j)
                            print(number, total, j)

    print(total)


main()
