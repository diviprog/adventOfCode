def parsenumbers(input, startnum, endnum):
    answer = []
    for i in range(startnum, endnum):
        numbers = []
        number = 0
        for j in range(len(input[i])):
            if input[i][j].isdigit():
                number = 10*number+int(input[i][j])
            elif input[i][j] == ' ':
                numbers.append(number)
                number = 0
        numbers.append(number)
        answer.append(numbers)

    return answer


def mapping(input_num, mapper):
    for i in mapper:
        if (input_num >= i[1]) and (input_num < i[1]+i[2]):
            return (i[0]+(input_num-i[1]))
    return input_num


def main():

    inf = open("input.txt", "r")
    input = []
    for i in inf:
        input.append(i[:-1])

    seed = input[0]
    seeds = []
    number = 0
    for i in range(7,len(seed)):
        if seed[i].isdigit():
            number = 10*number+int(seed[i])
        elif seed[i] == ' ' and number != 0:
            seeds.append(number)
            number = 0

    seedtosoil = parsenumbers(input, 3, 23)
    soiltofertiliser = parsenumbers(input, 25, 53)
    fertilisertowater = parsenumbers(input, 55, 87)
    watertolight = parsenumbers(input, 89, 121)
    lighttotemperature = parsenumbers(input, 123, 166)
    temperaturetohumidity = parsenumbers(input, 168, 202)
    humiditytolocation = parsenumbers(input, 204, 219)

    lowest = mapping(mapping(mapping(mapping(mapping(mapping(mapping(seeds[0], seedtosoil), soiltofertiliser), fertilisertowater), watertolight), lighttotemperature), temperaturetohumidity), humiditytolocation)
    for i in seeds[1:]:
        location = mapping(mapping(mapping(mapping(mapping(mapping(mapping(i, seedtosoil), soiltofertiliser), fertilisertowater), watertolight), lighttotemperature), temperaturetohumidity), humiditytolocation)
        if lowest > location:
            lowest = location

    print(lowest)


main()