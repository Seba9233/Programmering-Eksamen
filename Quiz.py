import random

def quizzen(selectedSymbol):
    if selectedSymbol == 1:
        number1 = random.randint(100, 999)
        number2 = random.randint(100, 999)
        print('Hvad er svaret på dette spørgsmål', number1, '+', number2)
        ans = int(input('Skriv svar her YY:'))

        if ans == number1 + number2:
            print('Correct!')
            quizzen(selectedSymbol)
        else:
            exit('You suck')

    elif selectedSymbol == 2:
        number1 = random.randint(2, 10)
        number2 = random.randint(2, 10)
        print('Hvad er svaret på dette spørgsmål', number1, '*', number2)
        ans = int(input('Skriv svar her XX:'))

        if ans == number1 * number2:
            print('Correct!')
            quizzen(selectedSymbol)
        else:
            exit('You suck')
