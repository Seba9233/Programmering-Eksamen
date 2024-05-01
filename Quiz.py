#import ???.txt
import random

questions = random.randint(100, 9999)
questions2 = random.randint(100, 9999)

def quizzen():
    print('Hvad er svaret på dette spørgsmål', questions, '+', questions2)
    ans=int(input('Skriv svar her:'))
    if ans==questions + questions2:
        print('yeee')
    else:
        exit('You fucking suck')

    #TODO
    #spørgsmål = parse_csv('???.txt') <--- CSV fil
    #randomize spørgsmål (og måske svar)
