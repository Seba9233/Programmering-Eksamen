import random

points = 0

def quizzen(selectedSymbol):
    global points
    if selectedSymbol == 1:
        number1 = random.randint(100, 999)
        number2 = random.randint(100, 999)
        print('Hvad er svaret på dette spørgsmål', number1, '+', number2)
        ans = int(input('Skriv svar her:'))

        if ans == number1 + number2:
            points += 1
            print(f"\033[3;32;1mKorrekt! Din score: {points}\033[0;0m \n")
            quizzen(selectedSymbol)
        else:
            print("\033[3;31;1mForkert. Din score:", points)
            exit('Du har tabt')

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