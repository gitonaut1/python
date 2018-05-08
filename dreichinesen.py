# -*- coding: cp1252 -*-

lied = "Drei Chinesen mit dem Kontrabass saßen auf der Straße und erzählten sich was. Da kam die Polizei, fragt‚ Was ist denn das? Drei Chinesen mit dem Kontrabass."
vokale = ["a", "e", "i", "o", "u", "ä", "ö", "ü"]
auswahl = raw_input('Auswahl Vokal (z.B. a,e,i,o,u,ä,ö,ü): ')
i = 0

while i < len(vokale)-1:
    lied = lied.replace(vokale[i], auswahl)
    i = i + 1

print lied
