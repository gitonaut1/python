# -*- coding: cp1252 -*-

lied = "Drei Chinesen mit dem Kontrabass sa�en auf der Stra�e und erz�hlten sich was. Da kam die Polizei, fragt� Was ist denn das? Drei Chinesen mit dem Kontrabass."
vokale = ["a", "e", "i", "o", "u", "�", "�", "�"]
auswahl = raw_input('Auswahl Vokal (z.B. a,e,i,o,u,�,�,�): ')
i = 0

while i < len(vokale)-1:
    lied = lied.replace(vokale[i], auswahl)
    i = i + 1

print lied
