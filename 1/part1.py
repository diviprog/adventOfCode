def main():
    inf = open("input.txt", "r")
    sum = 0
    for i in inf:
        num_digits = 0
        for j in i:
            if j.isdigit():
                if (num_digits==0):
                    first_dig = int(j)
                last_dig = int(j)
                num_digits+=1
        print(i, first_dig, last_dig)
        sum += 10*first_dig+last_dig

    print(sum)

main()