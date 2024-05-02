def vælgemne():
    valgemne = input("Vælg hvilket emne du vil have: \n"
                    "1 for plus\n"
                    "2 for gange")

    if valgemne == '1':
        print('Du vil nu få plus-spørgsmål')
        tegnet = '+'
        secondmenu(tegnet)

    elif valgemne == '2':
        print('Du vil nu få gange-spørgsmål')
        tegnet = '*'
        secondmenu(tegnet)

#randomized symbols