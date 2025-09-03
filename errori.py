





# vediamo qualche tipo di errori:

# print(a)
# 5 + "ciao"
# 5 / 0
# def func():
#     pass 


# try / except 
# esempio con funzione dividi 
# def dividi(num):
#     return 10 / num
# print("eseguo prima della chiamata di funzione")

# print(dividi(0)
# d
# print("eseguo dopo la chiamata di funzione")

# def dividi(num):
#     try:
#         return 10 / num
#     except:
#         return "c'è stato un errore e il blocco try non è stato eseguito"
    
# print("eseguo prima della chiamata di funzione")

# print(dividi(0))

# print("eseguo dopo la chiamata di funzione")


# esplicito è meglio di implicito 
# riprendiamo il caso precedente dove con except ho catturato tutti i possibili errori, ma non ho dato indicazioni sul tipo di errore 

# def dividi(num):
#     try:
#         return 10 / num
#     except ZeroDivisionError:
#         return "non puoi dividere per zero"
#     except TypeError:
#         return "hai passato un tipo di dato sbagliato"
    
# print("eseguo prima della chiamata di funzione")

# print(dividi("ciao"))

# print("eseguo dopo la chiamata di funzione")

#Conclusione blocco try / except :
# Se il codice nel blocco del try genera un’eccezione del tipo specificato dall’ except, allora il blocco dell’ except viene eseguito per gestirla. Se il codice nel blocco del try non genere un’ eccezione, o l’eccezione generata non è del tipo specificato dall’ except, allora l’eccezione si propaga e il blocco dell’ except viene ignorato. 

# proviamo con as ( e o err)
# def dividi (num):
#     try:
#         return 10 / num
#     except ZeroDivisionError as e :
#         return f"non puoi dividere per zero : {e}"
#     except TypeError as e:
#         return f"hai passato un tipo di dato sbagliato : {e}"
 
# print(dividi(0))
# print(dividi("ciao"))


# raise 
# def func(stringa):
#     if type (stringa) is not str: # oppure if type (stringa) != str:
#         raise TypeError ("devi passare una stringa")
#     return stringa.upper()

# print(func(3))

# possiamo intercettare l'errore con try / except
# def func(stringa):
#     try:
#         if type(stringa) is not str:
#             raise TypeError("devi passare una stringa come argomento")
#         return stringa.upper()
#     except TypeError as e:
#         return f"errore : {e}"
    
# print(func(3))
# print(func("ciao"))


# assertionError e assert 

# x = "ciao" 
# assert x  == "addio", "le due parole sono diverse"


# def saluta(nome):
#     assert nome =="dario", "saluto solo se il nome è dario"
#     return f"ciao{nome}"
# print(saluta("dario"))
# print(saluta("pippo"))


# num = "ciao"
# try:
#     print(10 / num)
# except ZeroDivisionError as e:
#     print(f"non puoi dividere per zero : {e}")

# except TypeError as e :
#     print(f"non puoi dividere per una stringa : {e}")

# else:
#     print("io vengo eseguito solo se nel blocco try non viene generata nessuna eccezzione ")
# finally:
#     print("io vengo eseguito sempre")

    
