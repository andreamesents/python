# lista = ["a", "b", "c"]
# print(enumerate(lista))

# for a in enumerate(lista):
#     print(a)

# for indice, lettera in enumerate(lista, start = 100):
#     print(f"la lettera{lettera} si trova ad indice {indice}")

# città = ["roma", "milano", "napoli"]
# latitudine = [41.9109, 45.4773, 40.863]
# longitudine = [ 12.4818, 9.1815, 14.2765]

# print(zip(città, latitudine, longitudine))

# print(list(zip(città, latitudine, longitudine)))

# for city, lat, lon in zip(città, latitudine, longitudine):
#     print(f"le coordinate di {city} sono {lat,lon}")

# func(["ciao", 1, 50, "A"])
# scrivi una funzione che accetta una lista e stampa ogni elemento della lista eccetto quello a indice 1 
# def func(lista):
#     for indice, elemento in enumerate(lista):
#         if indice ==1:
#             continue
#         print(elemento)
# func(["ciao", 1, 50, "A"])

# lista = ["roma", "milano", "napoli"]
# lista2= [1, 2, 3]
# print(list(zip(lista, lista2))) 

# lista = [(1,"A"), (2, "B"), (3, "C")]
# print(list(zip(*lista)))

# voglio ottenere una lista che contiene il numero di caratteri (la lunghezza) di ogni elemento di "nomi"

# nomi = ["andrea", "luigi", "marco"]
# nomi_len = [len(nome) for nome in nomi ]
# print(nomi_len)

# ora con map :
# nomi = ["andrea", "luigi", "marco"]
# print(map(len, nomi))
# print(list(map(len,nomi)))


# numeri = [1, 2, 3, 4, 5]
# squared = [ ] 
# for num in numeri:
#     squared.append(num **2)
# print(squared)

# def squared(num):
#     return num **2
# numeri = [1, 2, 3, 4, 5]
# squared = map(squared, numeri)

# print(squared)
# print(list(squared))

# voglio ottenere una lista formata da solo numeri pari 
# numeri = [ 1,2,3,4,5,6,7,8]
# pari = [ ] 
# for num in numeri:
#     if num %2 == 0:
#         pari.append(num)
# print(pari)

# numeri = [ 1,2,3,4,5,6,7,8]
# pari = [ num for num in numeri if num %2 ==0]
# print(pari)

# definisco prima la mia funzione di trasformazione
# questa funzione non deve restituire un "valore", ma un booleano true o false
# def pari(num):
#     return num %2 ==0

# print(pari(10))
# print(pari(3))
# numeri = [ 1,2,3,4,5,6,7,8]
# print(filter(pari, numeri))
# print(list(filter(pari, numeri)))

# def square(numero):
#     return numero **2
# print(square(5))

# def square (numero): return numero **2
# print(square(5))

# lambda numero : numero**2

# def square(numero):
#     return numero**2 
# numeri = [1,2,3,4,5] 
# squared = map(square,numeri)
# print(list(squared))

# numeri = [1,2,3,4,5]
# squared = map(lambda numero : numero**2, numeri)
# print(list(squared))

# def pari(numero):
#     return numero % 2 ==0 
# numeri = [1,2,3,4,5,6,7,8]
# print(list(filter(pari,numeri)))

# numeri = [1,2,3,4,5,6,7,8]
# list(filter(lambda numero: numero%2 ==0, numeri))

# def func (lista, lettera):
# lista_con_i = [ ] 
#     for elemento in lista:
#         if lettera("i") in elemento :
#             lista_con_i.append(elemento)
#     return lista_con_i
# print(func(["ciao, "andrea", "luigi", "marco"]))

    
# def func(lista, lettera):
#     lista_con_lettera = []
#     for elemento in lista:
#         if lettera in elemento:
#             lista_con_lettera.append(elemento)
#     return lista_con_lettera

# # Esempio di utilizzo
# print(func(["ciao", "andrea", "luigi", "marco"], "i"))

# l = [] 
# def func(lista, lettera):
#     return list(filter(lambda elemento : lettera in elemento, lista))
# print(func(["ciao", "andrea", "luigi", "marco"], "i"))

# def func (lista, lettera):
#     l = [ ] 
#     for elemento in lista:
#         if "i" in lettera:
#             l.append(elemento)
#     return l
# print(func(["ciao", "andrea", "luigi", "marco"], "i"))


# l= [ ]
# def func(lista, lettera):
#     for elemento in lista:
#         l.append(elemento.count(lettera))
#     return l
# print(func(["ciao", "andrea", "luigi", "marco"], "i"))

# l = [ ] 
# def func(lista, lettera):
#     return list(map(lambda elemento: elemento.count(lettera), lista))
# print(func(["ciao", "andrea", "luigi", "marco"], "i"))


# all
# print(all([1,2,3]))
# print(all([1,2,3,0]))
# print(all([ ] ))
# any 
# print(any([1,2,3,0]))

# print(min([1, 10, 100, 500])) # posso con una lista
# print(min(1, 10, 100, 500)) # posso con una sequenza di numeri
# print(min("a", "b", "c")) # posso con una sequenza di stringhe


# voglio sapere il max e il min in base al numero di caratteri :
# lista = [ "andrea", "marco", "ida", "francesco"]
# print(max(lista))
# print(min(lista))

# lista = [ "andrea", "marco", "ida", "francesco"]
# print(max(lista, key = lambda nome : len(nome)))
# print(min(lista, key = lambda nome : len(nome)))


# print(max("A", "B", "b", "a"))


# print(list(map(lambda stringa: stringa.lower(), ["ciao", "andrea", "Iva"])))


# def func (lista):
#     risultato = 0
#     for num in lista:
#         if num == float:
#         risultato += num
#         return risultato
# print(func([2.5, 3, 7, 1.5]))

def func(*args):
    return sum ([num for num in args if type(num) == float])
print(func(2.5, 3, 7, 1.5))

