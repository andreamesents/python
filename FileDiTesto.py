

# per leggere un file cosi come leggiamo un libro dobbiamo prima aprirlo (open) e poi leggerlo (read)

# f = open ("testo.txt")

# print(f.read())


# f.read()
# # non possiamo leggere un file piu di una volta

# # come riporto il cursore indietro??

# f.seek(0)
# print(f.read())
# # ora posso leggere il file piu di una volta

# # ora chiudo il file
# f.close()
# # non posso piu leggere il file


# # ora vediamo come leggere un file riga per riga se il file è troppo grande

# # readlinne e readlines 

# f = open ("testo.txt")

# f.readline()
# # legge la prima riga

# f.readline()
# # legge la seconda riga


# # invece con read lines legge tutto il file e lo mette in una lista

# f.readlines()
# # legge tutto il file e lo mette in una lista
# # ora chiudo il file
# f.close()
# # non posso piu leggere il file



# # statement with e opzioni di apertura 

# prima era : 

# f = open ("testo.txt")
# print(f.read())

# f.close()


# # meglio con questa sintassi alternativa 

# with open ("testo.txt") as f:
#     print(f.read())

# f.closed() 
# # ora il file è chiuso



# # opzione di apertura di un file 

# with open ("testo.txt") as f:
#     file = f.read()


# opzioni di apertura di un file 
# 'r' : lettura (default)
# 'w' : scrittura (sovrascrive il file)
# 'a' : scrittura (aggiunge al file)
# 'x' : scrittura (crea un nuovo file)




# scrivere un file di testo 

with open ("prova.txt", mode = "w") as file:
    file.write("ciao\n") # \n serve per andare a capo
    file.write("come va?\n") # \n serve per andare a capo

with open ("prova.txt") as file: 
    data = file.read()

print(data)

with open("prova.txt", mode="w") as file: 
    file.write("addio\n") # mi aspetto di aggiungere questa linea a quelle gia esistenti 

with open ("prova.txt") as file:
    data = file.read()

print(data)    

# in questo caso ho sovrascritto il file 
# ora vediamo come aggiungere al file senza sovrascrivere

with open ("prova.txt", mode = "a") as file: # a = append 
    file.write("aggiungi linea\n")

with open ("prova.txt") as file:
    data = file.read()
print(data)












