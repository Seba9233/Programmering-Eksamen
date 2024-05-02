import Quiz
import Emne
import QuizGange


def firstmenu():
    førstevalg = input("Tryk 1 for at åbne menuen")
    if førstevalg == '1':
        secondmenu()
    else:
        print("Wrong input")
        firstmenu()

def secondmenu(tegn):

    valg = input("Tryk 1 for at starte quizzen \n"
                    "Tryk 2 for at vælge et emne \n"
                    "Tryk 3 for at afslutte")

#    if tegn == '+':
 #       Quiz.quizzen()
  #  if tegn == '*':
   #     QuizGange.quizzenGange()


    if valg == '1':
        Quiz.quizzen()
    elif valg == '2':
        Emne.vælgemne()
    elif valg == '3':
        exit("Afsluttet! bozo...")
    else:
        secondmenu(tegn)
