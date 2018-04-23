from random import *
import time

runde = "y"

while True:
	spiel = ["Schere", "Stein", "Papier"]

	print ("    ***************************")
	time.sleep (0.2)
	print ("    * Schere - Stein - Papier *")
	time.sleep (0.2)
	print ("    ***************************")
	time.sleep (0.2)

	while True:
		spieler = input ("1 = Schere, 2 = Stein , 3 = Papier\n")
		if spieler > 0 and spieler < 4:
			break

	computer = randint(1,3)

	print "Spieler hat gewaehlt: " + spiel [spieler - 1]
	print "Computer hat gewaehlt: " + spiel [computer - 1]
	print "\n"
	time.sleep(0.5)

	if spieler == computer:
		print "unentschieden\n"

	if (spieler == 1) & (computer == 2):
		print ("Computer hat gewonnen\n")

	if (spieler == 1) & (computer == 3):
		print ("Spieler hat gewonnen\n")

	if (spieler == 2) & (computer == 1):
		print ("Spieler hat gewonnen\n")

	if (spieler == 2) & (computer == 3):
		print ("Computer hat gewonnen\n")
		
	if (spieler == 3) & (computer == 1):
		print ("Computer hat gewonnen\n")

	if (spieler == 3) & (computer == 2):
		print ("Spieler hat gewonnen\n")

	print "Moechten Sie noch einmal spielen? [beliebige Taste] oder [n]"
	runde = raw_input()
	if runde == "n":
		break
