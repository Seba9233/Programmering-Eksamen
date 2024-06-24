##module for tilfældige tal & sætter point
import random
points = 0

##selectedSymbol er et funktionskald. Hvis man vælger et symbol når man har trykket 2, ved den
#næste fil hvilket symbol spilllren har valgt.

def quizzen(selectedSymbol):
    global points
    if selectedSymbol == 1:
        #number 1 og 2 bruges til spørgsmål. Den tager en tilfældig integer fra 100 - 199
        number1 = random.randint(100, 999)
        number2 = random.randint(100, 999)
        #printer spørgsmålet
        print('Hvad er svaret på dette spørgsmål', number1, '+', number2)
        #ans er svaret som er et input
        ans = int(input('Skriv svar her:'))

        #hvis svaret er det samme som number1 + number2
        if ans == number1 + number2:
            #hvis man kommer videre giver den et point
            points += 1
            #teksten rundtom som eks. \033 og 3;32;1m er for at give teksten en farve og teksttype.
            #du kan google hvilken en i rækken 3;32;1m der gør hvad
            print(f"\033[3;32;1mKorrekt! Din score: {points}\033[0;0m \n")
            quizzen(selectedSymbol)
        else:
            print("\033[3;31;1mForkert. Din score:", points)
            exit('Du har tabt')

    #ellers hvis selectedSymbol == 2 bliver man stillet et spørgsmål med gange
    elif selectedSymbol == 2:
        number1 = random.randint(2, 10)
        number2 = random.randint(2, 10)
        print('Hvad er svaret på dette spørgsmål', number1, '*', number2)
        ans = int(input('Skriv svar her:'))

        if ans == number1 * number2:
            points += 1
            print(f"\033[3;32;1mKorrekt! Din score: {points}\033[0;0m \n")
            quizzen(selectedSymbol)
        else:
            print("\033[3;31;1mForkert. Din score:", points)
            exit('Du har tabt')