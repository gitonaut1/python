#Translating any word into Pig Latin! 
#Rules: Move the first letter of the word to the end and then append ay'. 
#Example: python -> ythonpay

vokale = ["a", "e", "i", "o", "u"]
runde = True

while runde:
	vokvorh = False
	original = raw_input('Get ready to start translating to Pig Latin!\nEnter a word: ')
	word = original.lower()

	if len(original) > 0 and original.isalpha():
		for i in range (0 , len(vokale)):   
			if (word[0] == vokale [i]):
				new_word = word + "ay"
				print (original)
				print (new_word)
				vokvorh = True
			else:
				i = i + 1
		if vokvorh == False:
			new_word = word[1:len(word)] + word[0] + "ay"
			print (original)
			print (new_word)
	else:
	  print ('empty')

	print "\nTry again? [y] oder [n]"
	
	#Entscheidung und Zulaesige Zeichen einschraenken
	while runde not in ("y", "n"):
		runde = raw_input()
	if (runde == "n"):
		runde = False
	else:
		runde = True
