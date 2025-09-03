# esercizi funzioni parte 1 
# definisci una funzione func che accetta una lista di numeri come parametro e come risultato restituisce la somma dei suoi parametri pari 
#func([1,2,3,4,5,6]) deve restituire 12(2+4+6)

# def func(lista):
#     result = 0
#     for num in lista:
#         if num %2 == 0:
#             result+= num
#     return result
# print(func([1,2,3,4,5,6])) # Questo dovrebbe stampare 12

# qual è l'output di questo codice ?
# def func(word):
#     contatore = 0
#     for lettera in word:
#         if lettera == "a":
#             contatore += 1
#         return contatore 
    
# print(func("paura"))

# quali sono gli output sei seguenti print statement ?
# def func(a, b= "A"):
#     return a *b 
# print(func(5))
# print(func(5,5))

# definisci una funzione func che puo ricevere un numero arbitrario di positional arguments e per ogni argomento la funzione deve stampare la sua lunghezza (len)
#  passa come argomenti solo delle stringhe 
# def func(*args):
#     for arg in args:
#         print(len(arg))
# func("ciao", "hello", "hola")
lista = [1,2,3,4,5,6,7,8,9,10]
def funzione_lista(lista):
    result = 0 
    num = 0 
    if num %2 ==0:
        print(num)
        result += num 
        return result
print(funzione_lista(lista))
    


