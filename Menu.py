import Quiz
import Emne

def firstmenu():
    førstevalg = input("Tryk 1 for at spille")
    if førstevalg == '1':
        secondmenu()
    else:
        print("Wrong input")
        firstmenu()

def secondmenu():
    valg = input(f"Tryk 1 for at starte quizzen \n"
                    f"Tryk 2 for at vælge et emne \n"
                    f"Tryk 3 for at afslutte")
    if valg == '1':
        Quiz.quizzen()
    elif valg == '2':
        Emne.vælgemne()
    elif valg == '3':
        exit("Afsluttet! bozo...")
    else:
        secondmenu()