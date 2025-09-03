# generatori:
# prima di parlare di generatori dobbiamo chiarire la differenza tra iteratori e iterabili in quanto i generatori sono anche degli iteratori 


# iteratore vs iterabile

# iteratore: 
# su di esso possiamo iterare 
# restituisce un elemento alla volta quando applichiamo next() su di esso 
# implementa l' iterator protocol (due metodi: __next__ e __iter__)


# iterabile: oggetto che restituisce un iteratore quando su di esso aplichiamo il metodo iter() 



# una lista non è un iteratore ma è un iterabile: 
# lista = [ 1,2,3] 
# next(lista) 
# print(dir(lista))

# l = iter(lista) 
# print(next(l))
# print(next(l))
# print(next(l))

# print(next(l)) # l'iteratore è esaurito




# una stringa non è un iteratore ma un iterabile :
# s = "ciao"
# next(s) # controllo se è un iteratore applicando next ()
# stringa = iter(s) # adesso stringa è un iteratore

# print(next(stringa)) # c
# print(next(stringa)) # i
# print(next(stringa)) # a
# print(next(stringa)) # o


# # print(next(stringa)) # l'iteratore è esaurito



# se una stringa non è un iteratore che succede quando uso for loop?? 

# s = "ciao" 
# for lettera in s: 
#     print(lettera) # c i a o


# possiamo rappresentare questo foorloop in questo modo : 
s = "ciao" 
iteratore = iter(s) # creo un iteratore 

while True: # parte un ciclo infinito da cui si esce quando l'iteratore si è esaurito 
    try: 
        item = next(iteratore) 
        print(item)
    except StopIteration: # quando l'iteratore è esaurito
        break







# come rendere un oggetto iterabile: 
# esempio, riprendiamo l'esercizio delle carte 

# class Carta(): 
#     def __init__ (self, valore, seme):
#         self.valore = valore 
#         self.seme = seme 

#     def __repr__ (self): 
#         return f" {self.valore} di { self.seme } " 


# class Mazzo():
#     def __init__ ( self): 
#         semi = ["bastoni", "coppe", "denari", "spade"] 
#         valori = [ "A", 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 

#         self.carte = [ Carta(valore, seme ) for seme in semi for valore in valori ]


# m = Mazzo() 

# for carta in m :
#     print(carta) # non funziona

# per farlo funzionare dobbiamo implementare il metodo __iter__ e __next__
# rivediamo l'esempio in modo corretto : 


# class Carta(): 
#     def __init__ (self, valore, seme):
#         self.valore = valore 
#         self.seme = seme 

#     def __repr__ (self): 
#         return f" {self.valore} di { self.seme } " 


# class Mazzo():
#     def __init__ ( self): 
#         semi = ["bastoni", "coppe", "denari", "spade"] 
#         valori = [ "A", 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 

#         self.carte = [ Carta(valore, seme ) for seme in semi for valore in valori ]

#     def __iter__(self): 
#         return iter(self.carte) # restituisce un iteratore che itera su self.carte
    


# m = Mazzo() 
# for carta in m :
#     print(carta)







# generatori : 
# un generatore è un iteratore 
# un generatore è una funzione che restituisce un iteratore 


# la sintassi è sempre la solita ma invece del **return**  statement i generatori usano la keyword ** yield** 
# restituiscono un object generator e non un valore come nelle funzioni co il return statement 


# def conta_fino_a_10 (): 
#     i = 0 
#     while i <= 10:
#         yield i # fa si che la funzione ritorni un valore, ma senza interrompere il ciclo della funzione 
#                 # la funzione si mette in pausa 
#         i += 1 

# g = conta_fino_a_10 ()
# print(g) 
# print(dir(g)) # vediamo che sono gia implementati i dunder methods next e iter 

# print(next(g)) # i generatori producono un elemento alla volta, non hanno problemi legati alla restrizione di memoria 
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g)) # l'iteratore è esaurito

# se voglio ottenere tutti gli elementi 
# list(g) 





# generator expression 

# abbiamo visto che nella definizione di una funzione era presente la keyword yield, automaticamente avevamo un generatore e la funzione restituiva un  generator object. 
# possiamo ottenere un jenerator object anche tramite le "list comprehension" dove invece di usare le parentesi quadre usiamo quelle tonde.

# list comprehension == otteniamo liste :
# l = [ num for num in range(1,10)] 
# print(type(l)) # <class 'list'>

# generator expression == otteniamo object generator : 

# g = (num for num in range (1,5))
# print(g) # <generator object <genexpr> at 0x7f8c4c0b5d60>

# essendo un generatore posso usare next fino a quando non esurisco l'iteratore 

# print(next(g)) # 1
# print(next(g)) # 2
# print(next(g)) # 3
# print(next(g)) # 4
# print(next(g)) # l'iteratore è esaurito




# modulo itertools
# i metodi di itertools si dividono in 3 categorie : 
# metodi per iteratori infiniti ( count, cycle, repeat)
# metodi per iteratori finiti ( accumulate, chain, stamp, zip_longest)
# metodi per calcolo combinatorio ( combinations, permutations, product)


# count: ci permette di contare all'infinito 

# from itertools import count 
# for num in count():
#     print(num) # vado a stampare tutti i numeri a partire da 0 all'infinito 

# quando utilizzo count è sempre meglio utilizzare un break statement per evitare di stampare all'infinito
# per esempio :

from itertools import combinations, count 
for num in count (start = 1, step = 10): 
    if num > 102 :
        break
    print(num)     


# chain: utilizzato per gestire più sequenze (piu iterabili) come se fossero una sequenza unica 

lista1 = [1,2,3] 
lista2 = [4,5,6,7,8]
lista3 = [9,10] 

from itertools import chain 
print(list(chain(lista1, lista2, lista3)))
# # output : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# metodo per il calcolo combinatorio: combinations

from itertools import combinatio
lista = [0, "A", 10, "B" ] 
combinazioni = combinations(lista, 2 )

for combinazione in combinazioni : 
    print(combinazione)
# output :
# (0, 'A')
# (0, 10)
# (0, 'B')
# ('A', 10)
# ('A', 'B')
# (10, 'B')


# se l'ordine delle nostre combinazioni è importante, allora useremo permutations 

from itertools import permutations 
lista = [0, "A", 10, "B" ]

permutazioni = permutations(lista, 2 )
for p in permutazioni : 
    print(p)
# output :
# (0, 'A')  
# (0, 10)
# (0, 'B')
# ('A', 0)
# (10, 0)























 









