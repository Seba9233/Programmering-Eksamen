#import ???.txt
import random
from Emne import tegnet

##FØRSTE TAL
number1 = random.randint(100, 9999)
number2 = random.randint(100, 9999)

def quizzen():
    print('Hvad er svaret på dette spørgsmål', number1, tegnet.Emne.vælgemne(), number2)
    ans=int(input('Skriv svar her:'))
    if ans==number1 + number2:
        print('Correct!')
    else:
        exit('You suck')

    #TODO (måske)
    #spørgsmål = parse_csv('???.txt') <--- CSV fil
    #tilføj multiple choice
