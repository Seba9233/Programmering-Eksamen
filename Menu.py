
#def point
class menu:

#MENU
    def __init__(self):
        valg = input(f"Tryk 1 for at starte quizzen \n"
                     f"Tryk 2 for at vælge et emne \n"
                     f"Tryk 3 for at afslutte")
        if valg == '1':
            print("Starter quizzen!")
            #startquiz()
        elif valg == '2':
            print("Vælg et emne!")
            #vælgemne()
        elif valg == '3':
            print("Afslutter...")
            #afslut()
        else:
            menu()


#vælg emne
    #def vælgemne

#afslut
    #def afslut