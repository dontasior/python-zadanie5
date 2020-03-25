

def main():
    x = int(input("W zakresie do której liczby całkowitej szukać liczb pierwszych? "))
    liczby = list(range(x - 1))
    for x in liczby:
        liczby[x] += 2
    print(liczby)
    #print([el for el in liczby if all(el % el1 !=0 for el1 in range(2, el))])
    print(liczby(map(
                 lambda el: el,
                 filter(lambda el: (all(el % el1 !=0 for el1 in range(2, el))), liczby)

    )))

if __name__ == '__main__':
    main()

