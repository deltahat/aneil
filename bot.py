import random
import sys

def generar_palabra():
	separador = "\n" #Nunca aparecera en una palabra, asi que sera el registro vacio.
	finoracion = (".", "!", "?", "\n") #Nueva finoracion si se encuentra al final de un string.
	seplinea  = "\n" #String used to seperate sentences

	# TABLA:
	w1 = separador
	w2 = separador
	table = {}

	#Archivo con logs:
	with open("twts.txt") as file:
	    for line in file:
	        for word in line.split():
	            if word[-1] in finoracion:
	                table.setdefault( (w1, w2), [] ).append(word[0:-1])
	                w1, w2 = w2, word[0:-1]
	                word = word[-1]
	            table.setdefault( (w1, w2), [] ).append(word)
	            w1, w2 = w2, word
	# Marca el final del archivo
	table.setdefault( (w1, w2), [] ).append(separador)

	# GENERA SECUENCIA DE OUTPUT
	maxfinoraciones  = 9

	w1 = separador
	w2 = separador
	sentencecount = 0
	sentence = []
	words = 0
	log = []
	aleatorio = random.randrange(9)

	## ALGORITMO:
	## CADENAS DE MARKOV
	## Sistema matematico que se transforma de un estado al otro,
	## con la propiedad de que el estado siguiente depende solo
	## de el estado actual, y no de los estados pasados.
	##
	## Estados: palabras
	## Estado actual: Ultimas dos palabras
	##
	## Se almacenan en una tabla valores [(p1, p2), px, py, pz...]
	## donde (p1, p2) son un par de palabras, y px, py, y pz son
	## posibles continuaciones leidas en algun tweet.
	## Los estados siguientes solo dependen de las dos ultimas
	## palabras, lo que puede llevar a resultados interesantes.

	#print "%d. " % (sentencecount+1),
	while sentencecount < maxfinoraciones:
	    if(words < 24):
	        newword = random.choice(table[(w1, w2)])
	        if newword == separador: sys.exit()
	        if newword in finoracion:
	            #print "%s%s%s" % (" ".join(sentence), newword, seplinea)
	            log.append(" ".join(sentence))
	            sentence = []
	            sentencecount += 1
	            #print "%d." % (sentencecount+1),
	        else:
	            sentence.append(newword)
	        w1, w2 = w2, newword
	        words += 1
	    else:
	        words = 0
	        #print "%s%s%s" % (" ".join(sentence), newword, seplinea)
	        log.append(" ".join(sentence))
	        sentence = []
	        sentencecount += 1
	        #print "%d." % (sentencecount+1),

	# Creando el tuit
	tuit = log[aleatorio]
	return tuit
