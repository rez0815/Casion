
# name: main.py
# Usage: main file of project 'Casino'
# Created by: rez0815
# Date: 2021-02-01


# input project 'BlackJack' later

import random
import time

games = ["BlackJack", "Other"]
print("Wilkommen im Casion!")
print("Wir freuen uns, sie hier begrüßen zu dürfen.")
knowgame = input("Wissen sie schon, welches Spiel sie spielen möchten? (y/n) ")

explain = True

while explain:
    if knowgame == "y":
        print("Sehr gut!")
        x = 1
        explain = False

    elif knowgame == "n":
        x = 1
        print("Kein Problem! Wir zeigen Ihnen gerne unser Angebot!")
        print("Unser aktuelles Angebot ist folgendes: ")
        print(games)
        explain = False

    else:
        print("Bitte nur mit y oder n antworten!")

run = True
while run:

    playgame = input("Welches Spiel möchten Sie spielen? ")

    if playgame == games[0]:
        print("Gute Wahl!")
        cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König", "Ass"]

        rules = input("Kennst du die Regeln bereits? (y/n): ")

        if rules == "n":
            print("Gut, kommen wir zu den Regeln: ")
            time.sleep(1)
            print("Ziel des Spiels ist, die Zahl 21 möglichst genau zu erreichen.")
            time.sleep(1)
            print("Nun zeigen wir ihnen die Wertigkeiten der Spielkarten: ")
            time.sleep(1)
            print("Die Karten mit den Zahlen haben den jeweils angeschriebenen Wert!")
            time.sleep(1)
            print("die 2 hat also auch den Wert 2, die 3 den Wert 3 usw.")
            time.sleep(1)
            print("Die 10, der Bub, die Dame und der König haben jeweils den Wert 10")
            time.sleep(1)
            print("Das Ass hat grundsätzlich den Wert 11")
            print("Sollten sie dadurch jedoch den Wert 21 übersteigen, so erhält es die Wertigkeit 1")
            time.sleep(1)
            print("Also gut, spielen wir!")
            a = 1

        elif rules == "y":
            print("Sehr gut!")
            a = 1

        else:
            print("Nur mit y oder n antworten, Bitte")
            a = 0

        if a == 1:

            playbj = True
            while playbj:

                playyn = input("Möchtest du spielen? (y/n)")

                if playyn == "y":
                    dcard1 = random.randint(0, 12)
                    dcard2 = random.randint(0, 12)

                    pcard1 = random.randint(0, 12)
                    pcard2 = random.randint(0, 12)

                    print("Die erste Karte des Dealers lautet:", cards[dcard1])
                    print("Die Zweite Karte des Dealers bleibt verdeckt. ")

                    print("Deine Karten lauten: ", cards[pcard1], cards[pcard2])

                    dscore = 0

                    if dcard1 < 9:
                        dscore = dscore + dcard1 + 2

                    elif dcard1 < 12:
                        dscore = dscore + 10

                    else:
                        if dscore < 11:
                            dscore = dscore + 11

                        else:
                            dscore = dscore + 1

                    if dcard2 < 9:
                        dscore = dscore + dcard2 + 2

                    elif dcard2 < 12:
                        dscore = dscore + 10

                    else:
                        if dscore < 11:
                            dscore = dscore + 11

                        else:
                            dscore = dscore + 1

                    pscore = 0

                    if pcard1 < 9:
                        pscore = pscore + pcard1 + 2

                    elif pcard1 < 12:
                        pscore = pscore + 10

                    else:
                        if pscore < 11:
                            pscore = pscore + 11

                        else:
                            pscore = pscore + 1

                    if pcard2 < 9:
                        pscore = pscore + pcard2 + 2

                    elif pcard2 < 12:
                        pscore = pscore + 10

                    else:
                        if pscore < 11:
                            pscore = pscore + 11

                        else:
                            pscore = pscore + 1

                    x = 0
                    while x == 0:

                        print("Dein Score beträgt: ", pscore)
                        morecard = input("Möchtest du noch eine Karte? (y/n)")

                        if morecard == "y":

                            nextcard = random.randint(0, 12)

                            if nextcard < 9:
                                pscore = pscore + nextcard + 2
                                print(cards[nextcard], "!")
                                time.sleep(1)

                            elif nextcard < 12:
                                pscore = pscore + 10
                                print(cards[nextcard], "!")
                                time.sleep(1)

                            else:

                                print(cards[nextcard], "!")
                                time.sleep(1)

                                if pscore < 11:
                                    pscore = pscore + 11

                                else:
                                    pscore = pscore + 1

                        elif morecard == "n":
                            print("Ok, dann schauen wir jetzt, was der Dealer so hat")
                            time.sleep(2)
                            x = 1

                        else:
                            print("ungültig")

                        if pscore > 21:
                            print(pscore)
                            print("Leider verloren")
                            time.sleep(2)
                            x = 2

                    if x == 1:
                        y = 0
                        while y == 0:

                            if dscore <= 17:

                                newdcard = random.randint(0, 12
                                                          )
                                if newdcard < 9:
                                    dscore = dscore + newdcard + 2
                                    print(cards[newdcard], "!")
                                    time.sleep(1)

                                elif newdcard < 12:
                                    dscore = dscore + 10
                                    print(cards[newdcard], "!")
                                    time.sleep(1)

                                else:
                                    print(cards[newdcard], "!")
                                    time.sleep(1)
                                    if dscore < 11:
                                        dscore = dscore + 11

                                    else:
                                        dscore = dscore + 1

                            else:
                                y = 1

                        if dscore > 21:
                            print("Gewonnen!")
                            print("Dein Score ist: ", pscore)
                            print("Der Score des Dealers ist: ", dscore)

                        else:
                            if pscore > dscore:
                                print("Gewonnen!")
                                print("Dein Score ist: ", pscore)
                                print("Der Score des Dealers ist: ", dscore)

                            elif dscore > pscore:
                                print("Leider verloren.")
                                print("Dein Score ist: ", pscore)
                                print("Der Score des Dealers ist: ", dscore)

                            else:
                                print("Unentschieden")
                                print("Dein Score ist: ", pscore)
                                print("Der Score des Dealers ist: ", dscore)

                elif playyn == "n":
                    print("Ok, dann nicht :/")
                    playbj = False

                else:
                    print("Nur mit y oder n antworten, bitte")

    elif playgame == games[1]:
        print("Tut mir leid, zur Zeit verfügen wir über keine weiteren Spiele.")

    elif playgame == "Keines":
        print("Oh, wie schade.")
        run = False

    else:
        print("Bitte mit einem Spiel antworten!")
