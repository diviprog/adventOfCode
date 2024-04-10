def main():
    inf = open("input.txt", "r")
    input = []
    for i in inf:
        input.append(i)

    time = 0
    for i in input[0][13:]:
        if i.isdigit():
            time = 10 * time + int(i)

    record = 0
    for i in input[1][12:]:
        if i.isdigit():
            record = 10 * record + int(i)

    count = 0
    for j in range(time):
        if j*(time-j) > record:
            count += 1
    print(count)

main()
