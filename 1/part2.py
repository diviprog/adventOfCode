numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}


def findLastDigit(line):
    for i in range(len(line), 0, -1):
        if line[i].isdigit():
            return int(line[i])
        for j in numbers.keys():
            if i - len(numbers[j]) >= 0:
                if numbers[j] == line[i - len(numbers[j]):i]:
                    return j
    return 0


def findFirstDigit(line):
    for i in range(len(line)):
        print(line[i])
        if line[i].isdigit():
            return int(line[i])
        for j in numbers.keys():
            if i + len(numbers[j]) <= len(line):
                if numbers[j] == line[i:i + len(numbers[j])]:
                    return j
    return 0


def findDigits(line):
    return findFirstDigit(line), findLastDigit(line)


def main():
    inf = open("input.txt", "r")
    total = 0
    for i in inf:
        first_dig, last_dig = findDigits(i)
        total += 10 * first_dig * last_dig

    print(total)


main()
