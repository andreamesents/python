


# numero = int(1)
# print(type(numero))
# # ho creato un oggetto che rappresenza l'istanza della classe interi 

# class StrumentiMusicali:
#     pass 

# chitarra = StrumentiMusicali() # è un istanza di StrumentiMusicali
# basso = StrumentiMusicali() # è un istanza di StrumentiMusicali

# print(type(chitarra))


# esempio: supponiamo di voler creare una classe che rappresenta l'idea della palla per fare sport 
# quindi creiamo una classe palla e da quella classe creiamo 3 diversi oggetti, 3 istanze della classe palla
# palla_basket, palla_tennis, palla_rugby

# possiamo pensare che ogni palla deve avere queste caratteristiche: colore, peso, diametro 
# questi sono attributi della classe "palla" 

# ad ognuno di questi attributi posso associare un valore, ad esempio per l'oggetto palla_tennis :
# colore = "giallo"
# peso = 55
# diametro = 6.5 

# colore peso diametro sono attributi della classe "palla"


# attributi = campi che specificano le caratteristiche o proprieta che tutti gli oggetti della classe devono avere.

# 2) per completare la caratterizzazione della nostra classe palla dobbiamo definire che tipo di azioni fara la palla 

# possono rimbalzare = definisco la funzione rimbalza()
# possono gonfiarsi = definisco la funzione gonfia()
# possono sgonfiarsi = definisco la funzione sgonfia()

# metodi = funzioni che specificano le azioni o i comportamenti che un oggetto della classe è in grado di compiere.


# creazione di una classe con metodo __init__

# class Persona:
#     def __init__(self, nome):
#         self.nome = nome

#     def salutare(self):
#         print("Ciao", self.nome)

# p1 = Persona()
# papa = Persona() 

# p1.nome = "Andrea"

# p1.cognome = "Mesentsev"

# p1.peso = 68 

# papa.nome = "Leonid"

# papa.cognome = "Mesentsev"

# papa.peso = 107 

# papa.salutare()




# class Persona():
#     pass 

# p1 = Persona()

# print(p1)

# p2 = Persona()

# print(p2)

# # definiamo alcuni attributi per la nostra classe nome cognome data di nascita

# # ci servira il costruttore __init__ che viene usato ogni volta che un istanza viene creata 

# class Persona:
#     def __init__(self):
#         pass

        
# p1 = Persona() # non devo passare niente perche gia ho messo self
# # self rappresenta l'istanza che stiamo creando 

# class Persona:
#     def __init__(self):
#         print(f" io sono {self}")

# p1 = Persona()

# print(p1)


# # ora vediamo come aggiungere attributi ad una classe 

# class Persona ():
#     def __init__(self):
#         pass 

# p1 = Persona()
# p2 = Persona()

# # aggiungiamo attributi per p1 e p2 

# p1. nome = "andrea"
# p2. nome = "Leonid"

# p1.cognome = "Mesentsev"

# print(p1.nome)
# print(p2.nome)

# print(p2.cognome)

# # sfruttiamo __init__
# # vogliamo garantire che ogni istanza della tessa classe abbia accesso agli stessi attributi 
# # utilizzeremo 'self' come riferimento dinamico alle nostre istanze 

# class Persona ():
#     def __init__(self,nome):
#         self.nome  = nome 

# p1 = Persona("Andrea")

# p2 = Persona("Leonid")

# print(p1.nome) 
# print(p2.nome) 

# attributi di istanza con valori di default 

# nome citta num_giocatori 

# class SquadraCalcio(): # definiamo la classe
#     def __init__(self, nome, città, num_giocatori = 22):            
#         self.nome = nome
#         self.città = città
#         self.num_giocatori = num_giocatori
#         self.punti = 0

#     def aggiungi_punti(self, punti):
#         self.punti += punti

#     # ora aggiungiamo qualche metodo 
#     # Metodo per simulare una partita
#     def gioca_partita(self, risultato):

#         if risultato == "vittoria":
#             self.aggiungi_punti(3)
#         elif risultato == "pareggio":
#             self.aggiungi_punti(1)
#         elif risultato == "sconfitta":
#             print(f"{self.nome} non ha guadagnato punti.")
#         else:
#             print("Risultato non valido.")
#         return risultato




# istanze con proprieta differenti 

# s1 = SquadraCalcio(nome = "roma", città = "roma")            
# s2 = SquadraCalcio(nome = "milan", città = "milano")
# s3 = SquadraCalcio(nome = "napoli", città = "napoli")

# print(s1.nome, s1.città, s1.num_giocatori) 
# print(s2.nome, s2.città, s2.num_giocatori)
# print(s3.nome, s3.città, s3.num_giocatori)

# print(s1.gioca_partita(risultato = "vittoria")) # roma ha guadagnato 3 punti



# class Chitarra ():
#     def __init__ (self, modello, marca, numero_corde = 6 ):
#         self.modello = modello 
#         self.marca = marca
#         self.numero_corde = numero_corde

# c1 = Chitarra (modello = "telecaster", marca = "fender")
# c2 = Chitarra (modello = "telecaster", marca = "fender", numero_corde = 7)

# print(c1.modello, c1.marca, c1.numero_corde) # telecaster fender 6
# print(c2.modello, c2.marca, c2.numero_corde) # telecaster fender 7



# metodo di una classe 

# class Persona:
#     def __init__(self, nome):
#         self.nome = nome

#     def salutare(self):
#         print("Ciao", self.nome)





# class SquadraCalcio ():
#     def __init__(self, nome, città, num_giocatori = 22): # valore di default per num_giocatori
#         self.nome = nome
#         self.città = città 
#         self.num_giocatori = num_giocatori 


#     def presentazione (self):
#         print(f"io sono la squadra: {self.nome}") 


#     def acquista (self, numero):
#         self.num_giocatori = self.num_giocatori + numero 

# s1 = SquadraCalcio (nome = "inter", città = "milano")

# print(s1.num_giocatori) 
# s1.acquista(numero = 5)

# print(s1.num_giocatori)
















# class lavoratore ():                                            #definisco proprieta e metodi nella classe 
#     def __init__ (self, stipendio = 2000): 
#         self.stipendio = stipendio 

#     def spesa (self, perdita):
#         self.stipendio -= perdita 
    

#     def bonus (self, aumento):
#         self.stipendio += aumento 
        
        





# l1 = lavoratore()
# print("Lavoratore1", l1.stipendio)
# l2 = lavoratore()
# print("Lavoratore2", l2.stipendio)


# l1.spesa(500)
# l2.spesa(1000)

# print("Lavoratore1", l1.stipendio)
# print("Lavoratore2", l2.stipendio)

# l1.bonus(1000)

# print("Lavoratore1", l1.stipendio)



