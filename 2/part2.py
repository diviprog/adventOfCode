def main():
    inf = open("input.txt", "r")

    power = lambda a, b, c: a*b*c

    total_power = 0
    for i in inf:
        max_red = 0
        max_green = 0
        max_blue = 0
        for j in range(len(i)):
            if i[j:j + 3] == "red":
                if i[j - 3].isdigit():
                    if max_red < 10*int(i[j - 3])+int(i[j - 2]):
                        max_red = 10*int(i[j-3])+int(i[j-2])
                else:
                    if max_red < int(i[j - 2]):
                        max_red = int(i[j-2])
            elif i[j:j + 5] == "green":
                if i[j - 3].isdigit():
                    if max_green < 10*int(i[j - 3])+int(i[j - 2]):
                        max_green = 10*int(i[j-3])+int(i[j-2])
                else:
                    if max_green < int(i[j - 2]):
                        max_green = int(i[j - 2])
            elif i[j:j + 4] == "blue":
                if i[j - 3].isdigit():
                    if max_blue < 10*int(i[j - 3])+int(i[j - 2]):
                        max_blue = 10*int(i[j-3])+int(i[j-2])
                else:
                    if max_blue < int(i[j - 2]):
                        max_blue = int(i[j - 2])

        total_power += power(max_red, max_blue, max_green)

    print(total_power)


main()
