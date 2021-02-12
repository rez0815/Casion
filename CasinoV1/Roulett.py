
# Roulett Game made for Project 'Casino'

import random
import time

yesno = input("Guten Tag! Interessiert? (y/n) ")

black = []
red = []
green = 0

for element in range(1, 37, 2):
    red.append(element)

for element in range(2, 37, 2):
    black.append(element)

print(red)
print(black)
if yesno == "y":

    knowrules = input("Kennen Sie die Regeln bereits? (y/n) ")

    know = True
    while know:

        if knowrules == "n":

            print("Kein Problem, wir erklären sie Ihnen gerne!")
            time.sleep(1)
            print("Zu Beginn der Runde setzen Sie ihren Einsatz.")
            time.sleep(1)
            print("Hierbei haben Sie verschiedene Möglichkeiten: ")
            time.sleep(1)
            print("Sie können beispielsweise auf Farben setzen (Rot / Schwarz / Grün)")
            time.sleep(1)
            print("Bei Rot oder Schwarz gewinnst du das Doppelte deines Einsatzes!")
            print("Bei Grün sogar das Zehnfache!")
            time.sleep(1)

            know = False

        elif knowrules == "y":
            print("Sehr gut! Fangen wir an!")
            know = False

        else:
            print("Nur mit y oder n antworten bitte!")

    con = input("Möchten Sie auf eine Farbe oder einen Zahlenbereich setzten? (c/n) ")

    if con == "c":

        colour = input("Schwarz, Rot oder Grün? (b/r/g) ")

        print("Gute Wahl!")

        randcolour = random.randint(0, 36)

        if randcolour in black:
            if colour == "b":
                print("Gewonnen!")

            else:
                print("Leider verloren.")

        elif randcolour in black:
            if colour == "r":
                print("Gewonnen!")

            else:
                print("Leider verloren.")

        else:
            if colour == "g":
                print("Gewonnen!")

            else:
                print("Leider verloren.")

    elif con == "n":

        print("Auf welchen Zahlenbereich möchten Sie setzten? ")
        print("1-12 = 'first' ")
        print("13-24 = 'second' ")
        print("25-36 = 'third' ")
        print("Eine Zahl = 'one' ")
        print("1-18 = 'fhalf' ")
        print("19-36 = 'shalf'")
        choose = input("Was wählen Sie? ")
        number = random.randint(0, 36)
        cnumber = 37

        if choose == "one":

            cnumber = int(input("Welche Zahl wählen Sie? (0-36) "))

        if number <= 12:

            if number == 0:

                if cnumber == 0:
                    print("Gewonnen!")

                else: print("Leider verloren!")

            elif choose == "first" or choose == "fhalf":
                print("Gewonnen!")

            elif cnumber == number:
                print("Gewonnen!")

            else:
                print("Leider verloren.")

        elif number <= 18:
            if choose == "fhalf" or choose == "second":
                print("Gewonnen!")

            else:
                print("Leider verloren.")

        elif number <= 24:

            if choose == "second" or choose == "shalf":
                print("Gewonnen!")

            elif cnumber == number:
                print("Gewonnen!")

            else:
                print("Leider verloren!")

        else:
            if choose == "third" or choose == "shalf":
                print("Gewonnen!")

            elif cnumber == number:
                print("Gewonnen!")

            else:
                print("Leider verloren.")

        if choose == "first" or choose == "second" or choose == "third":
            if number <= 12:
                print("first")

            elif number <= 24:
                print("second")

            else:
                print("third")

            print(number)
        elif choose == "fhalf" or choose == "shalf":

            if number <= 18:
                print("fhalf")

            else:
                print("shalf")

            print(number)

        else:
            print(number)