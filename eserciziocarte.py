


# 2 classi : carta e mazzo 

# per la classe carta: 

# ogni istanza deve avere un seme ("bastoni", "coppe", "denari", "spade")
# ogni asso deve avere un valore ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10") 
# dunder method repr deve restituire il valore della carta e il suo seme ("2 di denari", "A di bastoni",  ..._)



# per la classe mazzo:

# ogni istanza deve avere un attributo con tutte le possibili 40 combinazioni della classe carta 
# un metodo di istanza conta che deve restituire il numero delle carte rimanenti nel mazzo 
# dunder method repr che deve restituire informazioni si quante carte sono rimaste nel mazzo 
# un metodo di _distribuisci che accetta un numero e rimuove quel numero di carte dal mazzo 
# un metodo di istanza mischia (che deve mischiare ) con la funzione random 
# un metodo di istanza  distribuisci_carta che sfrrutta il metodo distribuisci 
# un metodo di istanza distribuisci_mano che riceve un numero come parametro e sfrutta il metodo distribuisci per distribuire un numero di carte dal mazzo e restituire la lista delle carte distribuite 




# d = Mazzo () 
# print(d.carte)
# d.mischia()
# print(d.carte)

# carta = d.distribuisci_carta()
# print(carta)

# mano = d.distribuisci_mano(3)
# print(mano)



class Carta(): 
    def __init__(self, valore, seme): 
        self.valore = valore 
        self.seme = seme 
        self.valori = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.semi = ["bastoni", "coppe", "denari", "spade"]
        
    def __repr__(self):
        return f"{self.valore} di {self.seme}"
    


c = Carta("A", "bastoni")
print(c)



from random import shuffle
class Mazzo():
    def __init__(self):
        semi = [ "bastoni", "coppe", "denari", "spade" ]
        valori = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10]

        self.carte = [Carta(valore, seme) for seme in semi for valore in valori]



    def conta(self):
        return len(self.carte)
    


    def __repr__(self):
        return f"mazzo di {self.conta()} carte"
    
    

    def _distribuisci(self, num ):
        count = self.conta()
        n_carte_da_distribuire = min([count, num])
        if count == 0:
            raise ValueError("non ci sono piu carte nel mazzo ")
        
        self.carte = self.carte [-n_carte_da_distribuire:]
        carte = self.carte[-n_carte_da_distribuire:] 
        return carte
    
    
    def mischia(self):
        if self.conta() < 40:
            raise ValueError("posso mischiare solo il mazzo con tutte le carte")
        shuffle(self.carte)

    def distribuisci_carta(self):
        return self._distribuisci(1)[0]
    
    def distribuisci_mano (self, num):
        return self._distribuisci(num)
    


        




d = Mazzo() 
print(d.carte)
d.mischia()
print(d.carte)
carta = d.distribuisci_carta()
print(carta)
mano = d.distribuisci_mano(5)
print(mano)
d.mischia()





