# first class object 
# 1 ad esempio lo è :

# a = 1 # assegno 1 ad una variabile che chiamo a 

# def func(num): # posso passare  1 come argomento e avere una funzione che restituisce 1 
#     return num 

# print(func(1))

# lista = [ 1, "A", "B"] # posso immagazzinare 1 allinterno di una lista 




# anche le funzioni hanno queste caratterisriche quindi sono dei first class objects 
# def potenza (a, b):
#     return a **b

# def calcola (func, a, b):
#     return func(a, b)

# print(calcola(potenza, 3, 6))

# def somma(a, b):
#     return a + b

# def moltiplicazione(a, b):
#     return a * b

# def calcola(func, a, b): # passo una funzione come argomento del parametro func
#     return func (a, b)

# print(calcola(somma, 3, 6))
# print(calcola(moltiplicazione, 3, 6))


# vediamo se una funzione puo essere restituita come output di un' altra funzione 

# import random 
# def saluta_persona (nome):
#     def segli_saluto ():
#         saluto = random.choice(["ciao", "addio", "arrivederci"])
#         return f"{saluto} {nome}"
#     return segli_saluto # restituisco la funzione scegli_saluto come output della funzione saluta_persona

# saluta = saluta_persona("dario")
# print(type(saluta)) # <class 'function'>
# print(saluta()) # ciao dario


# namespace e regola legb 
# namespace = struttura utilizzata per mappare ogni nome ad un oggetto creato nel nostro programma 
# esempio: a = 'dario' crea un nome simbolico (a) che si riferisce all'oggetto stringa 'dario' 

# come fa python a tenere traccia di tutti questi nomi simbolici ed evitare che interferiscano tra di loro?
# lo fa tramite i namespace
# i name space si occupano di collezionare tutti i nomi simbolici e i collegamenti agli oggetti a cui questi fanno riferimento.
# in parole povere siccome il namespace si occupa di effettuare una mappatura di nomi simbolici ad oggetti, possiamo vederlo come un dizionario dove le chiavi sono i nomi simbolici e i valori sono gli oggetti.

# in un progamma python ci sono 4 differenti tipi di namespaces: (LEGB)
# built-in
# global
# enclosing
# local

# #global: contiene tutti gli oggetti creati all'interno del programma principale 
# a = 10
# b = 20 
# lista = [a, b] 
# # ora a b e lista risiedono nel namespace global del file 

# enclosing e local: 
# prima python controlla se la funzione è definiti a livello locale senno enclosing senno globale 

# def enclosing_func():
#     x = 1 

#     def func_locale():
#         x = 100
#         return x 
#     return func_locale() # restituisco la funzione locale come output della funzione enclosing_func

# print(enclosing_func()) # 100
    
# ora pero se cancello la variabile x a livello locale

# def enclosing_func():
#     x = 1 

#     def func_locale():
        
#         return x 
#     return func_locale() 

# print(enclosing_func())
# # ottengo 1 dell'enclosing 

# ora se cancello la variabile enclosing :

# def enclosing_func():
    

#     def func_locale():
        
#         return x 
#     return func_locale() 

# print(enclosing_func())

# ottengo errore perchè non riesce a trovare x perche non lho definita al livello globale 



# x = 10
# def enclosing_func():
    

#     def func_locale():
        
#         return x 
#     return func_locale() 

# print(enclosing_func()) # 10 




