# per evitare errori possiamo utilizzare i keyword arguments
# print(sottrazione(a=10,b=5))
# print(sottrazione(b=5,a=10))

# default arguments
# def sottrazione (a,b):
#     return a-b
# sottrazione()
# se non passo nessun argomento ottengo un errore
# per evitare l'errore posso utilizzare i default arguments

# def sottrazione(a=0, b=0):
#     return a - b

# Chiamata alla funzione e stampa del risultato
# result = sottrazione(3, 4)
# print(result)  # Stampa: -1

# def func(*args):
#     return args

# print(func(1, 5, "A", "B", 500))

# def add (num1, num2, num3):
#     return num1 + num2 + num3
# add(1, 2, 3)
# print(add(1, 2, 3))
# #fino qui nulla di nuovo 
# #ora proviamo aggiungendo (1,2,3,4,5)
# def add (num1, num2, num3):
#     return num1 + num2 + num3
# add(1, 2, 3, 4, 5)
# print(add(1, 2, 3, 4, 5))
#otteniamo un errore   
#per evitare l'errore possiamo aggiungere altri parametri num4 e num5 
#oppure *args 
# def add (*args):
#     result = 0
#     for num in args :
#         result += num 
#     return result
# print(add(1, 2, 3, 4, 5))
# #oppure 
# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# primo caso 
# def add (a, *args):
#     result = 0 
#     for num in args:
#         result += num 
#     return result 
# print(add(1, 2, 3, 4, 5)) # Questo dovrebbe stampare 14

# def add(a, *args):
#     result = a  # Inizializza result con a
#     for num in args:
#         result += num 
#     return result 

# print(add(1, 2, 3, 4, 5))  # Questo dovrebbe stampare 15


# secondo caso 
# def add (*args, a ) :
#     result = 0
#     for num in args:
#         result += num
#     return result 
# print(add(1,2, a = 3))
# ora facciamo **kwargs e unpacking di un dizionario 

# def func(**kwargs):
#     print(kwargs)
# func(andrea = 25, gavriel = 26, david = 26, ruben = 25 )

# def func(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} ha {value} anni ")
# func(andrea = 25, gavriel = 26, david = 26, ruben = 25 )

# d1 = {"a":1, "b":2, "c":3}
# d2 = {"d":4, "e":5, "f":6}
# d3 = {**d1, **d2}
# print(d3)

# d1 = {"a":1, "b":2, "c":3}
# d2 = {**d1}
# print(d2)

# def add (a, b):
#     return (a +b)
# # ora trasfomro il dizionario in keyword argument 
# d = {"a":2, "b":3}
# print(add(**d))

# def func(a, *args, nome = "andrea", **kwargs):
#     print(a)
#     print(args)
#     print(nome)
#     print(kwargs)
# func(100, "a", "b", "c", citta = "roma", regione = "lazio")
# print(func)

# a = 100
# def func():
#     b = "andrea"
#     print(b)

# print(a)
# func()

# print(b)

# a = 100
# def func():
#     b = "andrea"
#     print(a + 100)
#     print(b)

# print(a)
# func() # Questo dovrebbe stampare 200 e "andrea"
# print(b) # Questo dovrebbe stampare un errore
# Questo codice stampa 100, 200 e "andrea" e poi un errore.
# La variabile a è globale, quindi è accessibile sia all'interno che all'esterno della funzione.
# La variabile b è locale, quindi è accessibile solo all'interno della funzione.

