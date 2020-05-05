"""
Die Caesar-Verschlüsselung ist ein einfaches Verschlüsselungsverfahren. Aus http://de.wikipedia.org/wiki/Caesar-Verschl%C3%BCsselung: 
Bei der Verschlüsselung wird jeder Buchstabe des Klartexts auf einen Geheimtextbuchstaben abgebildet. 
Diese Abbildung ergibt sich, indem man die Zeichen eines geordneten Alphabets um eine bestimmte Anzahl zyklisch nach rechts verschiebt (rotiert). 
Die Anzahl der verschobenen Zeichen bildet den Schlüssel, der für die gesamte Verschlüsselung unverändert bleibt.
Zum Beispiel wird der Klartext Python mit dem Schlüssel 2 in den Geheimtext Sbwkrq abgebildet.

Bei der Verschlüsselung wird jeder Buchstabe des Klartexts auf einen Geheimtextbuchstaben abgebildet. 
Diese Abbildung ergibt sich, indem man die Zeichen eines geordneten Alphabets um eine bestimmte Anzahl 
zyklisch nach rechts verschiebt (rotiert); zyklisch bedeutet, dass man beim Verschieben über Z hinaus 
wieder bei A anfangend weiterzählt. Die Anzahl der verschobenen Zeichen bildet den Schlüssel, 
der für die gesamte Verschlüsselung unverändert bleibt. 

Beispiel für eine Verschiebung um drei Zeichen:
Klar:    a b c d e f g h i j k l m n o p q r s t u v w x y z
Geheim:  D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
Aus dem Klartext „caesar“ wird somit der Geheimtext „FDHVDU“. 
Für die Entschlüsselung wird das Alphabet um dieselbe Anzahl Zeichen nach links rotiert.

Mathematisch lässt sich die Caesar-Verschlüsselung mit Hilfe der Modulo-Addition beschreiben. 
Hierzu werden zunächst alle Zeichen des Alphabets auf einen Restklassenring abgebildet, 
zum Beispiel a=0, b=1, c=2, …, z=25. Die Verschlüsselung eines Klartextbuchstabens 
P mit einer Verschiebung um K Zeichen und einem Alphabet mit 26 Zeichen ist dann definiert als:
    encryptK(P) = (P+K) mod26

Entschlüsselung von C:
    decryptK(C) = (C-K) mod26
"""
#Dict Erstellung
#alphabet = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,
#"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
alphabet = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",
14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}

def wahlvariante(): #Abfrage der Art und Weise der Ver- oder Entschlüsselung
    global variante
    variante = " "
    while variante != "V" and variante != "E":
        variante = input("Möchten Sie (V)er- oder (E)ntschlüsseln?: ")
        variante = str(variante)

def schluessel(): #Abfrage der Verschiebung / Verschlüsselung:
    global verschluesselung
    verschluesselung = 0
    while verschluesselung < 1 or verschluesselung > 26:
        verschluesselung = input("Welche Verschluesselung von 1-26 moechten Sie anwenden?: ")
        #if type(verschluesselung) != int:
        #    print("Keine Zahl") 
        verschluesselung = int(verschluesselung)
        if verschluesselung < 1:
            print("Wert zu klein")
        elif verschluesselung > 26:
            print("Wert zu groß")
    #return verschluesselung

def worteingabe(): #Abfrage Wort, kleinbuchstaben, keine Umlaute:
    global wort
    wort = " "
    while "ß" in wort or "ä" in wort or "ü" in wort or "ö" in wort or " " in wort:
        wort = input("Bitte Wort eingeben (keine Umlaute und ß), Groß-/Kleinschreibung ist egal: ")
        wort = wort.lower()

def verschluesseln():
    #wandelt das Wort in Zahl des Alphabetes um und verschiebt um x Stellen
    #bei Überang über Z / 26 wird bei 1 begonnen
    global verschluesselt
    verschluesselt=""
    for char in wort:
        for k, v in alphabet.items():
            if char == v:
                if k+verschluesselung <= 26:
                    verschluesselt = verschluesselt + alphabet[k+verschluesselung]
                else:
                    verschluesselt = verschluesselt + alphabet[k+verschluesselung-26]

def entschluesseln():
    global entschluesselt
    entschluesselt=""
    for char in wort:
        for k, v in alphabet.items():
            if char == v:
                if k-verschluesselung >= 1:
                    entschluesselt = entschluesselt + alphabet[k-verschluesselung]
                else:
                    entschluesselt = entschluesselt + alphabet[k-verschluesselung+26]

#Hauptprogramm
wahlvariante()
schluessel()
worteingabe()
if variante == "V":
    verschluesseln()
    print(verschluesselt.upper())
elif variante == "E":
    entschluesseln()
    print(entschluesselt)




"""

#wandelt das Wort in Zahl des Alphabetes um und verschiebt um x Stellen
#bei Überang über Z / 26 wird bei 1 begonnen
verschluesselt=[]
for char in wort:
    for k, v in alphabet.items():
        if char == k:
            v = v + verschluesselung
            if v > 26:
                v = v - 26
                verschluesselt.append(v)
            else:
                verschluesselt.append(v)

verschluesselt_wort = ""
for char in verschluesselt:
    for k, v in alphabet.items():
        if v == char:
            #verschluesselt_wort.append(char)
            verschluesselt_wort = verschluesselt_wort + char
print(verschluesselt_wort)
"""

#print(verschluesselt.upper())


#    for k, v in alphabet.items():
#        if k == wort[index]:
#            unverschluesselt.append(v)
#            index = index + 1

#druckt den Key /Buschstabe und die laufende Nummer:
#for k, v in alphabet.items():
#    print(k, v)

#druckt die laufende Nummer und den Key:
#for i, v in enumerate(alphabet):
#    print(i, v)