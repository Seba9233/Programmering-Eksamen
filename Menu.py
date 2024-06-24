#dette er menuen, den importer Quiz for at kunne sende brugeren videre til Quiz filen
import Quiz

#i denne funktion vælger man enten plus eller 1 fra menuen.
def chooseOperator():
    #definere et input
    chooseOperatorInput = input("Vælg hvilken type spørgsmål du vil have: \n"
                    "1 for plus\n"
                    "2 for gange\n")

    #hvis inputtet er 1 eller 2, vil den sende et 1 tal eller 2 tal til Quiz under funktionen "quizzen"
    if chooseOperatorInput == '1':
        print('Du vil nu få plus-spørgsmål')
        Quiz.quizzen(1)

    elif chooseOperatorInput == '2':
        print('Du vil nu få gange-spørgsmål')
        Quiz.quizzen(2)

    else:
        print('Ugyldigt input, prøv igen')
        return chooseOperator()

def menu():
    selectedSymbol = None
    while True:
        menuselection = input("Tryk 1 for at starte quizzen \n"
                    "Tryk 2 for at vælge et emne \n"
                    "Tryk 3 for at afslutte \n")

#hvis inputtet er 1, vil den sende det valgte symbol (selectedSymbol) til Quiz.quizzen
        if menuselection == '1':
            if selectedSymbol is not None:
                Quiz.quizzen(selectedSymbol)
        #ellers skal man vælge et emne først
            else:
                print('Vælg et emne først')
        if menuselection == '2':
            selectedSymbol = chooseOperator()

        elif menuselection == '3':
            exit("Afsluttet! bozo...")
        else:
            print('Ugyldigt input, prøv igen')
menu()